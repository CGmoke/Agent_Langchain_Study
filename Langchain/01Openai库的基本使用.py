import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
#通过打开文件的方式获取api_key，防止api_key暴露
with open("../api_key.txt", "r") as f:
    os.environ["QWEN_API_KEY"] = f.read()
llm = ChatOpenAI(
    model="qwen3-max",
    temperature=0.9,
    api_key=os.environ["QWEN_API_KEY"],
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
    )
response=llm.invoke([SystemMessage(content="You are a helpful assistant."), HumanMessage(content="帮我规划以下五一假期游玩?")])
print(response.content)

