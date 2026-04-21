from langchain_community.chat_models import ChatTongyi
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from markdown_it.rules_block import reference

from qwen_api_key import get_qwen_api_key

model = ChatTongyi(api_key=get_qwen_api_key(),model="qwen3-max")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "以我提供的以知参考资料为主,简洁和专业的回答用户问题，参考资料：{context}。"),
        ("human", "{input}")
    ]
)
vector_store = InMemoryVectorStore(
    embedding=DashScopeEmbeddings(model="text-embedding-v3",dashscope_api_key=get_qwen_api_key())
)

vector_store.add_texts(
    [
        "简介：当生命之神林星澜在神战中陨落，骸界的血月见证了他以灵骸双生之躯苏醒。",
        "吞噬灵能、篡改法则，他誓要撕开【归墟裂隙】重返故土，却发觉灵能枯竭竟是宇宙自愈的“断臂求生”——亿万种族争夺的残存高灵区，不过是熵增洪流中最后的泡沫。",
        "骸骨王座下，他背负神格碎片与归寂烙印，既是众生眼中的救世主，亦是熵增规则的化身。",
        "当时间闭环将暗算真相碾碎成悖论，当人族主神的背叛与骸界至高的追杀交织成网，他必须抉择：以神骸为祭重启文明火种，还是化身归寂与万物同亡？"
     ]
)
input_text = "简介介绍了什么"
result=vector_store.similarity_search(input_text, k=4)
reference_text = '['
for i in result:
    reference_text += i.page_content + ','
reference_text+=']'

def print_prompt(prompt):
    print(prompt.to_string())
    print("="*20)
    return prompt
chain = prompt | print_prompt|model | StrOutputParser()

ans=chain.invoke({"input": input_text, "context": reference_text})
print(ans)