"""
基于Streamlit完成web网页上传服务
"""
import time

import streamlit as st
from knowledge_base import KnowledgeBaseService
st.set_page_config(page_title="知识库更新服务",page_icon="📚")
st.title("知识库更新服务")

uploader_file=st.file_uploader(
    "上传txt文件",
     type=[ "txt"],#限定上传文件类型
     accept_multiple_files=False,#仅接受一个文件上传
)
if "service" not in st.session_state:
    st.session_state['service']= KnowledgeBaseService()

"""
上传文件
"""
if uploader_file:
    file_name = uploader_file.name
    file_type = uploader_file.type
    file_size = uploader_file.size/1024

    st.subheader(f"文件名：{file_name}")
    st.write(f"文件类型：{file_type},文件大小：{file_size:.2f}KB")
    #获取上传文件内容get_value->bytes->decode('utf-8')
    text = uploader_file.getvalue().decode('utf-8')
    with st.spinner("载入知识库中..."):
        #上传文件
        time.sleep(1)
        res = st.session_state['service'].upload_by_str(text,file_name)
        st.success(res)
