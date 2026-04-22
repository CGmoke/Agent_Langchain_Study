import json
import os
from typing import Sequence
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import messages_from_dict, message_to_dict, BaseMessage

import config_data as config


def get_history(session_id):
    """获取历史消息"""
    return FileChatMessageHistory(session_id,'./chat_history')



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

