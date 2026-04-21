from langchain_community.llms.ollama import Ollama
from langchain_ollama import ChatOllama, OllamaLLM

# 方式 1: 使用聊天模型（推荐，更适合对话）
chat_model = ChatOllama(model="qwen2.5:7b", temperature=0.7)
response = chat_model.invoke("你是谁？")
print("ChatOllama 响应:")
print(response.content)
print("\n" + "="*50 + "\n")

# 方式 2: 使用纯语言模型
llm_model = OllamaLLM(model="qwen2.5:7b", temperature=0.7)
response_text = llm_model.invoke("你是谁？")
print("OllamaLLM 响应:")
print(response_text)
