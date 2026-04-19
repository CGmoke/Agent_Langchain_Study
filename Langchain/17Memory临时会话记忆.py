from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from qwen_api_key import get_qwen_api_key

model = ChatTongyi(api_key=get_qwen_api_key(), model="qwen-max")
#通用提示词模板
# prompt = PromptTemplate.from_template(
#     "你需要根据会话历史回应用户问题。对话历史：{chat_history}，用户提问:{input},请回答"
# )
ChatPromptTemplate = ChatPromptTemplate.from_messages(
    [
        ("system", "你需要根据会话历史回应用户问题。"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
    ]
)
#str构建解析器
str_parser = StrOutputParser()

base_chain = ChatPromptTemplate | model | str_parser

store={}#key是会话id，value是InMemoryChatMessageHistory类对象
#通过会话id获取InMemoryChatMessageHistory类对象
def get_history(session_id):
    """获取历史消息"""
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()

    return store[session_id]
#创建一个新链，对原有链增强功能，自动附加历史消息
conversation_chain = RunnableWithMessageHistory(
    base_chain,#被增强的原有chain
    get_session_history=get_history,#通过会话id获取InMemoryChatMessageHistory类对象
    input_messages_key="input",      #表示用户输入在模板中的占位符
    history_messages_key="chat_history",
)

if __name__ == "__main__":
    session_config = {
        'configurable':{
            "session_id":"user_001"
        }
    }
    res =conversation_chain.invoke({"input":"小明有2只猫"},session_config)
    print(res)
    res =conversation_chain.invoke({"input":"小刚有1只狗"},session_config)
    print(res)
    res =conversation_chain.invoke({"input":"总共有几只宠物"},session_config)
    print(res)