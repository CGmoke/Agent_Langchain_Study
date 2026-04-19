from langchain_community.chat_models.tongyi import ChatTongyi
import  os
with open("../api_key.txt", "r") as f:
    os.environ["QWEN_API_KEY"] = f.read().strip()
model = ChatTongyi(api_key=os.environ["QWEN_API_KEY"], model="qwen-max")
messages = [
    ('system', "你是一个边塞诗人"),
    ('human', "写一首唐诗"),
    ('ai', "请稍等，正在生成中..."),
    ('human', "请再给我写一首唐诗"),
]
# 简写形式有点，减少导包，支持变量注入
res = model.stream(input=messages)
for i in res:
    print(i.content, end="",flush= True)