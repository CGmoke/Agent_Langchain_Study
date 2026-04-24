import os
from langchain_chroma import Chroma
from utils.file_handler import TextLoader, PyPDFLoader, listdir_with_allowed_type,get_file_mad5_hex
from utils.config_handler import chroma_conf
from model.factory import  embedding_model
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from utils.logger_handler import logger
from utils.path_tool import get_abs_path
class VectorStoreService:
    def __init__(self):
        self.vector_store =Chroma(
            collection_name=chroma_conf["collection_name"],
            embedding_function= embedding_model,
            persist_directory=chroma_conf["persist_directory"]
        )
        self.spliter = RecursiveCharacterTextSplitter(
            chunk_size=chroma_conf["chunk_size"],
            chunk_overlap=chroma_conf["chunk_overlap"],
            separators=chroma_conf["separators"],
            length_function=len,
        )
    def get_retriever(self):
        return self.vector_store.as_retriever(search_kwargs = {"k": chroma_conf["k"]})
    def load_document(self, file_path:str = None):
        """
        从数据文件夹内读取数据文件，转为向量存入向量库
        要计算文件的MD5去重
        :param file_path: 文件路径（可选，默认使用配置文件中的路径）
        :return:None
        """
        def check_md5_hex(md5_for_check:str):
            """
            检查文件是否已经处理过
            :param md5_hex: 文件的MD5
            :return:
            """
            if not os.path.exists(get_abs_path(chroma_conf["md5_hex_store"])):
                open(get_abs_path(chroma_conf["md5_hex_store"]),"w",encoding="utf-8").close()
                return False #文件不存在
            with open(get_abs_path(chroma_conf["md5_hex_store"]),"r",encoding="utf-8") as f:
                md5_hex_list = f.readlines()
            for line in md5_hex_list:
                line = line.strip()
                if line == md5_for_check:
                    return True#文件已经处理过
                return False#文件没有处理过

            return None

        def save_md5_hex(md5_for_check:str):
            """
            保存文件的MD5
            :param md5_hex: 文件的MD5
            :return:
            """
            with open(get_abs_path(chroma_conf["md5_hex_store"]),"a",encoding="utf-8") as f:
                f.write(md5_for_check+'\n')

        def get_file_documents(read_path:str):
            """
            获取文件的内容
            :param read_path: 文件路径
            :return:
            """
            if read_path.endswith('txt'):
                return TextLoader(read_path, encoding="utf-8").load()
            if read_path.endswith('pdf'):
                return PyPDFLoader(read_path).load()
            return []
        allowed_files_path :list[ str] = listdir_with_allowed_type(get_abs_path(chroma_conf["data_path"]),tuple(chroma_conf["allow_konwledge_file_type"]))
        for path in allowed_files_path:
            file_md5_hex = get_file_mad5_hex(path)
            if check_md5_hex(file_md5_hex):
                logger.info(f"[加载知识库]文件{path}已经存在知识库中，请勿重复添加")
                continue
            try:
                documents:list[Document]= get_file_documents(path)
                if not documents:
                    logger.warning(f"[加载知识库]文件{path}内没有有效文本内容，跳过")
                    continue
                split_documents:list[Document] = self.spliter.split_documents(documents)
                if not split_documents:
                    logger.warning(f"[加载知识库]文件{path}分片后没有有效文本内容，跳过")
                    continue
                #添加向量
                self.vector_store.add_documents(split_documents)
                #记录已处理文件md5值
                save_md5_hex(file_md5_hex)
                logger.info(f"[加载知识库]文件{path}内容加载成功")
            except Exception as e:
                #exc_info为True会记录详细的报错堆栈，如果为False仅记录错误信息
                logger.error(f"[加载知识库]文件{path}加载失败，错误信息：{str(e)}",exc_info= True)

if __name__ == '__main__':
    vector_store = VectorStoreService()
    vector_store.load_document()
    retriever = vector_store.get_retriever()
    for i in retriever.invoke("迷路"):
        print(i)