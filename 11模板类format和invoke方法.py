from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import FewShotPromptTemplate
from langchain_core.prompts import ChatPromptTemplate
"""
PromptTemplate->StringPromptTemplate->BasePromptTemplate
FewShotPromptTemplate->StringPromptTemplate->BasePromptTemplate
ChatPromptTemplate->BaseChatPromptTemplate->BasePromptTemplate
"""
prompt_template=PromptTemplate.from_template('我的邻居姓{lastname}，刚生了{gender}，你帮我起个名字，简单回答。')
res1=prompt_template.format(lastname="杨",gender="男")
print(res1,type(res1))
res2=prompt_template.invoke({"lastname":"杨","gender":"男"})
print(res2,type(res2))