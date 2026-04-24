import streamlit as st

from agent.react_agent import ReactAgent

st.title("智扫通机器人智能客服")
st.divider ()

if 'agent' not in st.session_state:
    st.session_state['agent'] = ReactAgent()
if 'message' not in st.session_state:
    st.session_state['message'] = [{
        "role": "assistant",
        "content": "你好，有什么可以帮助你？"
    }]
for message in st.session_state['message']:
    with st.chat_message(message["role"]):
        st.write(message["content"])
# 用户输入
prompt  = st.chat_input("请输入您的问题：")
if prompt:
    st.chat_message("user").write(prompt)
    st.session_state["message"].append({
        "role": "user",
        "content": prompt
    })
    response_messages = []
    with st.spinner("智能客服思考中..."):
        res_stream = st.session_state['agent'].executive_stream(prompt)
        def capture(generator,cache_list):
            for chunk in generator:
                cache_list.append(chunk)
                yield chunk
        st.chat_message("assistant").write(capture(res_stream,response_messages))
        st.session_state["message"].append({
            "role": "assistant",
            "content": response_messages[-1]
        })
        st.rerun ()