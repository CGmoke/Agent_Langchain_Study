from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path="../data/公考通·公务员考试岗位智能查询系统创业计划书.pdf",
    mode="single",
)
i=0
for doc in loader.lazy_load():
    i+=1
    print(doc)
    print(i)