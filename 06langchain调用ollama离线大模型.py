# 导入LangChain的Ollama聊天模型和消息类型
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import time

# 创建Ollama模型实例，指定使用qwen2.5:7b模型
model = ChatOllama(
    model="qwen2.5:7b",
    temperature=0.7,  # 设置温度参数控制创造性
    num_ctx=4096,     # 设置上下文窗口大小
)

# 构建对话消息列表，包含系统提示和多轮对话历史
messages = [
    SystemMessage(content="你是一个边塞诗人"),  # 系统消息定义AI角色
    HumanMessage(content="写一首唐诗"),          # 用户第一轮请求
    AIMessage(content="请稍等，正在生成中..."),   # AI的第一轮回复
    HumanMessage(content="请再给我写一首唐诗"),   # 用户第二轮请求
]
try:
    # 调用模型的stream方法进行流式输出
    print("正在生成回答...")
    res = model.stream(input=messages)
    
    # 逐块读取并打印流式响应内容
    for i in res:
        print(i.content, end="", flush=True)
    
    print("\n\n生成完成！")

except Exception as e:
    print(f"\n❌ 发生错误: {e}")
    print("\n🔧 可能的解决方案:")
    print("1. 检查Ollama服务是否正常运行: ollama serve")
    print("2. 确保模型已正确安装: ollama list")
    print("3. 尝试重启Ollama服务")
    print("4. 检查系统内存是否充足")
    print("5. 尝试使用更小的模型")
