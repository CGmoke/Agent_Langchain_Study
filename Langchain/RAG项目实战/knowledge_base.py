"""
知识库
"""
from datetime import datetime
import os
import config_data as config
import hashlib
from langchain_chroma.vectorstores import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
def check_md5(md5_str: str):
    """
    检查传入的md5字符串是否已经被传入
    return:False 未处理过，True 已处理
    """
    if not os.path.exists(config.md5_path):
        #如果未存在，那该文件未处理过
        open(config.md5_path,'w',encoding='utf-8').close()
        return  False
    else:
        for line in open(config.md5_path,'r',encoding='utf-8').readlines():
            line=line.strip() #处理字符串前后空格和回车
            if line==md5_str:
                return True
        return False


def save_md5(md5_str: str):
    """将传入的md5字符串，记录到文件内报存"""
    with open(config.md5_path,'a',encoding='utf-8') as f:
        f.write(md5_str+'\n')
def get_string_md5(input_str: str,encoding='utf-8'):
    """将传入的字符串转化为md5字符串"""

    #将字符串转换为bytes字节值
    str_bytes=input_str.encode( encoding=encoding)
    #创建md5对象
    md5_obg = hashlib.md5()
    md5_obg.update(str_bytes)
    return md5_obg.hexdigest()



class KnowledgeBaseService():
    """"""
    def __init__(self):
       #如果文件夹不存在创建数据库文件夹，如果存在则不跳过
       os.makedirs(config.persist_directory,exist_ok=True)
       self.chroma = Chroma(
           collection_name=config.collection_name,
           embedding_function=DashScopeEmbeddings(model=config.embedding_model,dashscope_api_key=config.qwen_api_key),
           persist_directory=config.persist_directory, #数据库本地存储文件夹

       )   #向量存储实例Chroma向量库对象
       self.spliter = RecursiveCharacterTextSplitter(
           chunk_size=config.chunk_size,#分割后的文本段最大长度
           chunk_overlap=config.chunk_overlap,#连续文本段之间的字符重叠数量
           separators=config.separators,#分割的分隔符
           length_function=len,#统计字符的函数
       )  #文本分割器的对象

    def upload_by_str(self,data: str,filename: str):
        """上传字符串,进行向量化，存入向量数据库中"""
        #先得到md5值
        md5_hex = get_string_md5(data)
        if check_md5(md5_hex):
            # print(f"{filename}已经处理过")
            return "文件已处理"
        if len(data)>config.max_split_char_size:
            # print(f"开始对{filename}进行文本分割")
            #进行文本分割
            texts: list[str] = self.spliter.split_text(data)

        else:
            texts = [data]
            # print(f"{filename}长度小于{config.max_split_char_size}，不进行分割")
        ids = [f"{filename}_{i}" for i in range(len(texts))]
        metadata = {
            "source": filename,
            "create_time":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        # 将文本向量化
        self.chroma.add_texts(
            texts,
            metadatas=[metadata for _ in texts],
            ids=ids
        )
        # 保存md5值
        save_md5(md5_hex)
        return "上传成功"

if __name__ == '__main__':
    service = KnowledgeBaseService ()
