import json
from langchain_community.document_loaders import JSONLoader

# loader = JSONLoader(
#     file_path="data/stu.json",
#     jq_schema='.',
#     text_content=False,
# )
# documents = loader.load()
# for document in documents:
#     print(json.dumps(document.page_content,ensure_ascii= False,indent=2),type(document))
loader = JSONLoader(
    file_path="../data/stu_json_lines.json",#文件路径
    jq_schema='.',#json的schema，jq语法解析器，必填
    text_content=False,#判断内容是否为字符串内容，默认为True
    json_lines=True,#判断文件格式是否为json lines
)
document = loader.load()
print(document)