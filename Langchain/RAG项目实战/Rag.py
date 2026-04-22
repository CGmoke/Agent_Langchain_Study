from logging import config
from langchain_community.chat_models import ChatTongyi
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate, format_document, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory, RunnableLambda
from vector_stores import VectorStoreService
import config_data as config
from langchain_core.output_parsers import StrOutputParser
from file_history_store import get_history



def print_prompt(prompt: str):
    """打印prompt"""
    print(f"prompt: {prompt.to_string()}")
    return prompt
class RagService(object):

    def __init__(self):
        self.vector_store = VectorStoreService(
            DashScopeEmbeddings(
                model=config.embedding_model,
                dashscope_api_key=config.qwen_api_key
            )
        )
        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", "以我提供的以知参考资料为主,简洁和专业的回答用户问题，参考资料：{context}。"),
                ("system","并且我提供的用户对话历史记录如下："),
                MessagesPlaceholder(variable_name="chat_history"),
                ("user", "请回答用户问题：{input}"),
            ]
        )
        self.chat_model = ChatTongyi(
            api_key=config.qwen_api_key,
            model=config.chat_model
        )
        self.chain = self.__get_chain()

    def __get_chain(self):
        """获取最总执行链"""
        retriever = self.vector_store.get_retriever()

        def format_document(docs:list[Document]):
            if  not docs:
                return "无相关参考资料"
            formatted_str = ""
            for doc in docs:
                formatted_str += f"文档片段: {doc.page_content}\n文档元数据: {doc.metadata}\n\n"
            return formatted_str
        def format_for_retriever(value:dict)->str:
            print("-----------------------",value)
            return value['input']

        def format_for_prompt(value:dict):
            new_value={}
            new_value['input'] = value['input']['input']
            new_value['context'] = value['context']
            new_value['chat_history'] = value['input']['chat_history']
            return new_value


        chain =(
            {
                "input": RunnablePassthrough (),
                "context":RunnableLambda(format_for_retriever)|retriever|format_document,
            }
            | RunnableLambda(format_for_prompt)|self.prompt_template| print_prompt|self.chat_model| StrOutputParser()
        )
        conservation_chain = RunnableWithMessageHistory(
            chain,
            get_history,
            input_messages_key="input",
            history_messages_key="chat_history",
        )
        return conservation_chain

if __name__ == '__main__':
    """session_id配置"""
    session_config ={
        "configurable": {
            "session_id": "user_001",
        },
    }
    res = RagService().chain.invoke({"input":"夏天穿什么颜色衣服"}, session_config)
    print(res)