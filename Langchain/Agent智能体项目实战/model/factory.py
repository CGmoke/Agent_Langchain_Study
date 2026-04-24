"""
模型工厂
提供模型
"""
from abc import ABC, abstractmethod
from typing import Optional
from langchain_core.embeddings import Embeddings
from  langchain_community.chat_models.tongyi import BaseChatModel
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.chat_models import ChatTongyi
from utils.config_handler import rag_conf
from qwen_api_key import get_qwen_api_key
class BaseModelFactory(ABC):
    """
    模型工厂
    """
    @abstractmethod
    def generator(self)->Optional[Embeddings |BaseChatModel]:
        """
        生成模型
        """
        pass

class ChatModelFactory(BaseModelFactory):
    """
    聊天模型工厂
    """
    def generator(self) ->Optional[Embeddings |BaseChatModel]:
        return ChatTongyi(
            api_key=get_qwen_api_key(),
            model=rag_conf["chat_model_name"]
        )

class EmbeddingModelFactory(BaseModelFactory):
    """
    嵌入模型工厂
    """
    def generator(self) ->Optional[Embeddings |BaseChatModel]:
        return DashScopeEmbeddings(
            model=rag_conf["embedding_model_name"],
            dashscope_api_key=get_qwen_api_key()
        )

chat_model = ChatModelFactory().generator()
embedding_model = EmbeddingModelFactory().generator()