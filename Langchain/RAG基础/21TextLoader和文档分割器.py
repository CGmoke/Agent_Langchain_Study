from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loder = TextLoader("../../data/TextLoader测试数据.txt", encoding="utf-8")
docs = loder.load()
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,#分段的最大字符数
    chunk_overlap=0,#分段间允许的重叠字符数
    separators=["\n\n", "\n", ".", ",", "!", "?", "!", "?", "。", "！", "？", "！", "？"],
    length_function=len,#统计字符的依据函数
)
split_docs = text_splitter.split_documents(docs)
print(len(split_docs))
for doc in split_docs:
    print(doc.page_content)
