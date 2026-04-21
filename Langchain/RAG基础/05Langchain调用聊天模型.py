from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage
import  os
with open("../../api_key.txt", "r") as f:
    os.environ["QWEN_API_KEY"] = f.read()
model = ChatTongyi( api_key=os.environ["QWEN_API_KEY"],model="qwen-max")
messages = [
    SystemMessage(content="你是一个边塞诗人"),
    HumanMessage(content="写一首唐诗"),
    AIMessage(content="请稍等，正在生成中..."),
    HumanMessage(content="请再给我写一首唐诗"),
]
res = model.stream(input=messages)
for i in res:
    print(i.content, end="",flush= True)
