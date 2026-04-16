from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Tongyi
from qwen_api_key import get_qwen_api_key
prompt_template=PromptTemplate.from_template('我的邻居姓{lastname}，刚生了{gender}，你帮我起个名字，简单回答。')
model = Tongyi(api_key=get_qwen_api_key(), model="qwen-max")
#使用prompt_template方法，在项目中更加规范地使用模板，避免硬编码
chain = prompt_template | model
print(chain.invoke({"lastname": "杨", "gender": "男"}))