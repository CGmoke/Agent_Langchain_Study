from langchain_community.llms.tongyi import Tongyi
import  os
with open("../../api_key.txt", "r") as f:
    os.environ["QWEN_API_KEY"] = f.read()
model =Tongyi(api_key=os.environ["QWEN_API_KEY"], model="qwen-max")
res=model.stream(input="你是谁,你能做什么？")
for i in res:
    print(i,end="",flush=True)