from streamlit import session_state

from qwen_api_key import get_qwen_api_key


md5_path = "./md5.txt"
# chroma
collection_name = "rag"
persist_directory = "./chroma_db"

#spliter
chunk_size = 500
chunk_overlap = 50
separators=["\n\n", "\n", ".", ",", "!", "?", "!", "?", "。", "！", "？", "！", "？"]
max_split_char_size = 1000   #文本分割阈值

#相似度检索阈值
similarity_threshold = 1 #检索返回匹配的文档数量

#模型配置
embedding_model = "text-embedding-v3"
chat_model = "qwen3-max"
qwen_api_key = get_qwen_api_key()

session_config ={
        "configurable": {
            "session_id": "user_001",
        },
    }