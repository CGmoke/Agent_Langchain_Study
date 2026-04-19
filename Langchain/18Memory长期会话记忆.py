import json
import os
from typing import Sequence
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import messages_from_dict, message_to_dict, BaseMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from qwen_api_key import get_qwen_api_key

#messages_to_dict:单个消息对象（BaseMessage类示例）->字典
#messages_from_dict:字典->消息对象

class FileChatMessageHistory(BaseChatMessageHistory):
    """基于文件的会话历史记录"""
    def __init__(self,seddion_id,storage_path):
        self.session_id = seddion_id    #会话id
        self.storage_path = storage_path    #不同会话id的存储文件，所在文件夹的存储路径
        #完整文件路径
        self.file_path = os.path.join(self.storage_path,self.session_id)
        #确保文件夹是存在的
        os.makedirs(os.path.dirname(self.file_path),exist_ok=True)

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        #sequence 是python内置的序列类型，比如列表、元组、字符串等等。
        all_messages = list(self.messages)      #已有的消息列表
        all_messages.extend(messages)#添的和已有的融合成一个列表

        #将数据同步写入到本地文件中
        #类对象写入文件 ->二进制
        # new_messages=[]
        # for message in all_messages:
        #     new_messages.append(message_to_dict(message))
        new_messages = [message_to_dict(message) for message in all_messages]

        with open(self.file_path,"w",encoding="utf-8") as f:
            json.dump(new_messages,f)
    """将messages转化为字典"""
    @property   #@property装饰器将messages方法变成成员属性用
    def messages(self)->list[BaseMessage]:
        #当前文件内：list[字典]
        try:
            with open(self.file_path,"r",encoding="utf-8") as f:
                messages_data = json.load(f)
                return messages_from_dict(messages_data)
        except FileNotFoundError:
            return []
    """清空文件"""
    def clear(self) -> None:
        with open(self.file_path,"w",encoding="utf-8") as f:
            json.dump([],f)



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

# store={}#key是会话id，value是InMemoryChatMessageHistory类对象
#通过会话id获取InMemoryChatMessageHistory类对象
def get_history(session_id):
    """获取历史消息"""
    return FileChatMessageHistory(session_id, "../chat_history")


#创建一个新链，对原有链增强功能，自动附加历史消息
conversation_chain = RunnableWithMessageHistory(
    base_chain,#被增强的原有chain
    get_history,#通过会话id获取InMemoryChatMessageHistory类对象
    input_messages_key="input",      #表示用户输入在模板中的占位符
    history_messages_key="chat_history",
)

if __name__ == "__main__":
    session_config = {
        'configurable':{
            "session_id":"user_001"
        }
    }
    # res =conversation_chain.invoke({"input":"小明有2只猫"},session_config)
    # print(res)
    # res =conversation_chain.invoke({"input":"小刚有1只狗"},session_config)
    # print(res)
    res =conversation_chain.invoke({"input":"总共有几只宠物"},session_config)
    print(res)