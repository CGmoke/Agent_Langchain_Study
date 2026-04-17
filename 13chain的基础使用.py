from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.runnables.base import RunnableSerializable
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

model = ChatTongyi(api_key=get_qwen_api_key(), model="qwen-max")

#组成链，要求每一个组件都是runnable接口的子类
chain = chat_prompt_template | model
res = chain.invoke(input={"chat_history":history_data}).content
print( res)

#通过stream流式输出

for chunk in chain.stream(input={"chat_history":history_data}):
    print(chunk.content, end="",flush=True)