"""
streamlit web端智能体
"""
import streamlit as st
from Rag import RagService
import config_data as config

#标题
st.title("线上服装购买智能客服")
st.write("欢迎来到线上服装购买智能客服,请输入您需要咨询的问题。")
st.divider()#分割线


if "message" not in st.session_state:
    st.session_state["message"] = [{
        "role": "assistant",
        "content": "你好，有什么可以帮助你？"
    }]
if 'rag' not in st.session_state:
    st.session_state["rag"] = RagService()

for message in st.session_state["message"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])
#输入框
prompt = st.chat_input("请输入您的问题：")
if prompt:
    #智能客服输入问题
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state["message"].append({"role": "user", "content": prompt})
    #输出结果
    res_list = []
    with st.spinner("正在思考中..."):
        res_stream = st.session_state['rag'].chain.stream({"input": prompt},config.session_config)

        def capture_output(generator,cache_list):
            for chunk in generator:
                cache_list.append(chunk)
                yield chunk


        with st.chat_message("assistant"):
            st.write_stream(capture_output(res_stream, res_list))
        st.session_state["message"].append({"role": "assistant", "content":"".join(res_list) })