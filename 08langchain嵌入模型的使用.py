from langchain_community.embeddings import DashScopeEmbeddings
from qwen_api_key import get_qwen_api_key
embed = DashScopeEmbeddings(dashscope_api_key=get_qwen_api_key(), model="text-embedding-v1")
print(embed.embed_query("你好"))
print(embed.embed_documents(["你好"]))