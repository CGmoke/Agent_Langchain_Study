from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.document_loaders import CSVLoader
from langchain_chroma import Chroma
from qwen_api_key import get_qwen_api_key
vector_store = Chroma(
    collection_name="info",#当前向量存储名
    embedding_function=DashScopeEmbeddings(model="text-embedding-v3",dashscope_api_key=get_qwen_api_key()),
    persist_directory="./data/chroma"

)

loder = CSVLoader(file_path="../data/info.csv",
                   encoding="utf-8",
                  source_column="source.info",
                   )
documents = loder.load()
#向量存储的新增，添加，检索
vector_store.add_documents(
    documents= documents,
    ids= ["id"+str(i) for i in range(1,len(documents)+1)],
)
#删除，传入[id,id...]
vector_store.delete(["id1","id2"])
#检索
result = vector_store.similarity_search(
    query="骸骨",
    k=2
)
print(result)