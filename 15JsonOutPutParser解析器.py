from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from qwen_api_key import get_qwen_api_key
"""
模型输入：PromptValue 或字符串或序列（BaseMessage、list、tuple、str、dict）
模型输出：AIMessage
提示词模板输入：要求是字典
提示词模板输出：PromptValue对象
"""
str_parser = StrOutputParser()#AiMessage输入、str输出
json_parser = JsonOutputParser()#AiMessage输入、dict输出
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

#构建链
chain = prompt_1 | model | json_parser| prompt_2 | model | str_parser
for chunk in chain.stream(input={"lastname":"杨","gender":"男"}):
    print(chunk, end="",flush=True)

