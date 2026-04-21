from langchain_community.document_loaders import CSVLoader


loader = CSVLoader(file_path="../../data/stu.csv",
                   encoding="utf-8",
                   csv_args={
                       "delimiter": ",",
                       "quotechar": '"',
                       "fieldnames":[]}
                   )

#批量加载.load () -> [document,document....]

# documents = loader.load()
# for document in documents:
#     print(document,type(document))

#懒加载 .lazy_load () -> 迭代器[document]
for document in loader.lazy_load():
    print(document,type(document))