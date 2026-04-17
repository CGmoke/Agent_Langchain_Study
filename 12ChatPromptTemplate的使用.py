from cffi import model
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi
from qwen_api_key import get_qwen_api_key
chat_prompt_template=ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个边塞诗人，可以作诗."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "请再来一首诗"),
    ]
)
history_data = [
    ('human','你来写一首唐诗'),
    ('ai','床前明月光，疑是地上霜，举头望明月，低头思故乡'),
    ('human','请再给我写一首唐诗'),
    ('ai','锄禾日当午，汗滴禾下入，谁知盘中餐，粒粒皆辛苦'),
]
prompt_text=chat_prompt_template.invoke(input={"chat_history":history_data}).to_string()
# print(res)
model = ChatTongyi(api_key=get_qwen_api_key(), model="qwen-max")
res = model.invoke(prompt_text).content
print(res)
