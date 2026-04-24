"""
文件处理
"""
import hashlib
import os
from langchain_core.documents import Document
from sqlalchemy.ext.asyncio import result
from utils.logger_handler import logger
from langchain_community.document_loaders import PyPDFLoader,TextLoader
def get_file_mad5_hex(file_path: str):
    """
    获取文件md5的16进制字符串
    :return:
    """
    if not os.path.exists(file_path):
        logger.error(f"文件：{file_path}不存在")
        return
    if not os.path.isfile(file_path):
        logger.error(f"路径：{file_path}不是文件")
        return
    md5_obj = hashlib.md5()
    chunk_size = 4096
    try:
        with open(file_path, "rb") as f:
            md5_obj.update(f.read())
            while chuk:=f.read(chunk_size):
                md5_obj.update(chuk)
            hash_code = md5_obj.hexdigest()
            return hash_code
    except Exception as e:
        logger.error(f"文件：{file_path}读取失败，错误信息：{str(e)}")
        return

def listdir_with_allowed_type(path: str, allowed_types: tuple[str]):
    """
    返回文件夹内的文件夹列表（允许的文件后缀）
    :return:
    """
    files = []
    if not os.path.isdir(path):
        logger.error(f"[listdir_with_allowed_type]路径：{path}不是文件夹")
        return allowed_types

    for f in os.listdir(path):
        if f.endswith(allowed_types):
            files.append(os.path.join(path, f))

    return  tuple(files)

def pdf_loader(file_path: str,password= None)-> list[Document]:
    """
    pdf文件加载
    :return:
    """
    return PyPDFLoader(file_path,password).load()


def txt_loader(file_path: str)-> list[Document]:
    """
    txt文件加载
    :return:
    """
    return TextLoader(file_path).load()
