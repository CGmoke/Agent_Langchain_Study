from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from qwen_api_key import get_qwen_api_key
from langchain_community.chat_models.tongyi import ChatTongyi

str_parser = StrOutputParser()
json_parser = JsonOutputParser()
model = ChatTongyi(api_key=get_qwen_api_key(), model="qwen3-max")
#第一个提示词模板
prompt_1 = PromptTemplate.from_template(
    "我的邻居姓{lastname}，刚生了{gender}，你帮我起个名字，并封装为Json格式返回给我，"
    "要求key是name，value就是你起的名字，请严格按照要求执行。"
)
#第二个提示词模板
prompt_2 = PromptTemplate.from_template(
    "姓名：{name}，请帮我解析含义。"
)
#自定义函数
msg_fun=RunnableLambda(lambda ai_message: {"name": ai_message.content})
chain = prompt_1 | model |msg_fun| prompt_2 | model | str_parser
for chunk in chain.stream(input={"lastname":"杨","gender":"男"}):
    print(chunk, end="",flush=True)