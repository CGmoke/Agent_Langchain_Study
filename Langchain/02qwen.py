from langchain_community.llms.tongyi import Tongyi
import  os
with open("../api_key.txt", "r") as f:
    os.environ["QWEN_API_KEY"] = f.read()
model = Tongyi(api_key=os.environ["QWEN_API_KEY"], model="qwen-turbo")
res  = model.invoke("你是谁")
print(res)