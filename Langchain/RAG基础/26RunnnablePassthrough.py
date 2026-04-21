import sys
import os
# 将项目根目录添加到系统路径，以便导入 qwen_api_key 模块
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_community.chat_models import ChatTongyi
from langchain_core.runnables import RunnablePassthrough
from langchain_core.vectorstores import InMemoryVectorStore
from dashscope_embedding_compat import DashScopeEmbeddingCompat
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document
from qwen_api_key import get_qwen_api_key

model = ChatTongyi(api_key=get_qwen_api_key(),model="qwen3-max")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "以我提供的以知参考资料为主,简洁和专业的回答用户问题，参考资料：{context}。"),
        ("human", "{input}")
    ]
)
vector_store = InMemoryVectorStore(
    embedding=DashScopeEmbeddingCompat(model="text-embedding-v2", api_key=get_qwen_api_key())
)
# 向量存储的初始化,传入一个list[str]
vector_store.add_texts(
    [
        "简介：当生命之神林星澜在神战中陨落，骸界的血月见证了他以灵骸双生之躯苏醒。",
        "吞噬灵能、篡改法则，他誓要撕开【归墟裂隙】重返故土，却发觉灵能枯竭竟是宇宙自愈的“断臂求生”——亿万种族争夺的残存高灵区，不过是熵增洪流中最后的泡沫。",
        "骸骨王座下，他背负神格碎片与归寂烙印，既是众生眼中的救世主，亦是熵增规则的化身。",
        "当时间闭环将暗算真相碾碎成悖论，当人族主神的背叛与骸界至高的追杀交织成网，他必须抉择：以神骸为祭重启文明火种，还是化身归寂与万物同亡？"
     ]
)
input_text = "简介介绍了什么"
#langchain中向量存储对象，有一个方法：as_retriever,可以返回一个Runnable接口的子类实例对象
retriever=vector_store.as_retriever(search_kwargs={"k":4})#k表示返回的向量个数

def format_func(docs: list[Document]):
    if not docs:
        return ""
    reference_text = '['
    for i in docs:
        reference_text += i.page_content + ','
    reference_text+=']'
    return reference_text

chain = (
    {"input":RunnablePassthrough(),"context":retriever|format_func } | prompt | model | StrOutputParser()
)
ans=chain.invoke({"input": input_text})
"""
retriever:
    -输入：用户的提问   str
    -输出：向量库的检索结果    list[document]
prompt：
    -输入：用户的提问+向量库的检索结果  dict
    -输出：完整的提示词  PromptValue
"""
print(ans)