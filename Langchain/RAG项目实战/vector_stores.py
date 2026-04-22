from langchain_chroma import Chroma
import config_data as config

class VectorStoreService(object):
    def __init__(self,embedding):
        """
        :param embedding:嵌入式模型传入
        """
        self.embedding = embedding

        self.vector_store = Chroma(
            collection_name=config.collection_name,
            persist_directory=config.persist_directory,
            embedding_function=self.embedding,
        )

    def get_retriever(self):
        """
        :return: Chroma的retriever对象
        """
        return self.vector_store.as_retriever(search_kwargs={"k": config.similarity_threshold})


if __name__ == '__main__':
    from langchain_community.embeddings import DashScopeEmbeddings
    embedding = DashScopeEmbeddings(model=config.embedding_model,dashscope_api_key=config.qwen_api_key)
    service = VectorStoreService(embedding)
    retriever = service.get_retriever()
    result = retriever.invoke("我的体重180斤，请提供尺码推荐")
    print(result)