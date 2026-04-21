from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate
from langchain_community.llms.tongyi import Tongyi
from qwen_api_key import get_qwen_api_key
example_template =PromptTemplate.from_template("单词：{word},反义词:{antonym}")

#示例的动态数据注入，要求list内部套字典
example_data=[
    {"word":"good","antonym":"bad"},
    {"word":"happy","antonym":"sad"}
]
few_shot_prompt=FewShotPromptTemplate(
    example_prompt=example_template,    #示例数据的模板
    examples = example_data,         #示例的数据，list内套字典
    prefix="告知我单词的反义词，给我提示如下例子",            #示例之前的提示词
    suffix="基于前面的示例告知我，{input_word}的反义词是？",            #示例之后的提示词
    input_variables=["input_word"],     #声明在前缀或后缀中所需注入的变量名
)
res=few_shot_prompt.invoke(input={"input_word":"左"}).to_string()
print(res)
model = Tongyi(api_key=get_qwen_api_key(), model="qwen-max")
print(model.invoke(res))