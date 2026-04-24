"""
RAG总结服务：用户提问，搜索参考资料，将提问和参考资料提交给模型，让模型总结回复
"""
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from rag.vector_store import VectorStoreService
from utils.prompt_loader import load_rag_prompts
from model.factory import ChatModelFactory
from langchain_core.output_parsers import StrOutputParser

def print_prompt(prompt):
    """打印prompt"""
    print(20*"-")
    print(prompt.to_string())
    print(20*"-")
    return prompt
class RagSummaryService(object):
    def __init__(self):

        self.vector_store = VectorStoreService()
        self.retriever = self.vector_store.get_retriever()
        self.prompt_text = load_rag_prompts()
        self.prompt_template = PromptTemplate.from_template(self.prompt_text)
        self.model = ChatModelFactory().generator()
        self.chain = self.__init__chain()
    def __init__chain(self):
        """
        初始化链
        :return:
        """
        chain = self.prompt_template|print_prompt|self.model|StrOutputParser()
        return chain
    def retriever_docs(self,query:str)->list[Document]:
        """
        获取参考资料
        :param query:
        :return:
        """
        return self.retriever.invoke(query)
    def rag_summarize(self,query:str)->str:
        """
        RAG总结
        :param query:
        :return:
        """
        context_docs=self.retriever_docs(query)
        context = ""
        counter = 0
        for doc in context_docs:
            counter+=1
            context+=f"[参考资料{counter}]: 参考元数据:{doc.metadata['source']}|参考内容: {doc.page_content}\n"
        return self.chain.invoke({"input":query,"context":context})

if __name__ == '__main__':
    rag = rag_service = RagSummaryService()
    print(rag.rag_summarize("小户型如何使用扫地机器人"))