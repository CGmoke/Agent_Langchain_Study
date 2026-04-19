from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from qwen_api_key import get_qwen_api_key
#构建解析器
parser = StrOutputParser()
model = ChatTongyi(api_key=get_qwen_api_key(), model="qwen-max")
prompt = PromptTemplate.from_template("我的邻居姓{lastname}，刚生了{gender}，你帮我起个名字，简单回答。")
chain = prompt | model |parser |model| parser

res = chain.invoke(input={"lastname":"杨","gender":"男"})
print(res,type(res))