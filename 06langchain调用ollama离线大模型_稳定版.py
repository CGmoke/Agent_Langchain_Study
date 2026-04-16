"""
Ollama 离线大模型调用 - 稳定版本
直接调用 Ollama API，避免 langchain-ollama 库的兼容性问题
"""

# 导入必要的库
import requests
import json
from typing import List, Dict, Generator


class OllamaClient:
    """
    Ollama 客户端类，封装了与 Ollama API 的交互逻辑
    提供流式和非流式两种调用方式
    """
    
    def __init__(self, base_url: str = "http://localhost:11434", model: str = "qwen2.5:7b"):
        """
        初始化 Ollama 客户端
        
        参数:
            base_url: Ollama 服务的基础 URL
            model: 要使用的模型名称
        """
        self.base_url = base_url  # 保存服务地址
        self.model = model        # 保存模型名称
        self.chat_url = f"{base_url}/api/chat"  # 构建聊天API的完整URL
    
    def chat_stream(
        self,
        messages: List[Dict[str, str]],
        system_prompt: str = None,
        temperature: float = 0.7
    ) -> Generator[str, None, None]:
        """
        流式聊天方法，逐块返回生成的内容
        
        参数:
            messages: 对话消息列表，每条消息包含 role 和 content
            system_prompt: 可选的系统提示词
            temperature: 温度参数，控制输出的随机性
            
        返回:
            生成器，逐块产出文本内容
        """
        # 构建完整的消息列表
        full_messages = []
        
        # 如果提供了系统提示，添加到消息列表开头
        if system_prompt:
            full_messages.append({
                "role": "system",
                "content": system_prompt
            })
        
        # 添加用户提供的对话消息
        full_messages.extend(messages)
        
        # 构建请求数据 payload
        payload = {
            "model": self.model,           # 指定使用的模型
            "messages": full_messages,     # 完整的对话历史
            "stream": True,                # 启用流式输出
            "temperature": temperature,    # 设置温度参数
        }
        
        # 设置请求头，指定 JSON 格式
        headers = {
            "Content-Type": "application/json"
        }
        
        try:
            # 发送 POST 请求到 Ollama 聊天 API
            response = requests.post(
                self.chat_url,
                json=payload,
                headers=headers,
                stream=True,    # 使用流式响应
                timeout=120     # 设置超时时间为120秒
            )
            
            # 检查响应状态码是否成功
            response.raise_for_status()
            
            # 逐行读取并解析流式响应
            for line in response.iter_lines():
                if line:  # 如果行不为空
                    data = json.loads(line)  # 解析 JSON 数据
                    
                    # 提取并返回消息内容
                    if 'message' in data and 'content' in data['message']:
                        content = data['message']['content']
                        yield content  # 使用生成器逐块返回内容
                    
                    # 检查生成是否完成
                    if data.get('done', False):
                        break  # 结束流式输出
        
        except requests.exceptions.RequestException as e:
            # 捕获网络请求相关的异常
            raise Exception(f"Ollama API 请求失败: {e}")
        
        except json.JSONDecodeError as e:
            # 捕获 JSON 解析异常
            raise Exception(f"JSON 解析错误: {e}")
    
    def chat(
        self,
        messages: List[Dict[str, str]],
        system_prompt: str = None,
        temperature: float = 0.7
    ) -> str:
        """
        非流式聊天方法，一次性返回完整的生成内容
        
        参数:
            messages: 对话消息列表
            system_prompt: 可选的系统提示词
            temperature: 温度参数
            
        返回:
            完整的生成文本字符串
        """
        # 收集流式输出的所有内容
        full_response = ""
        
        # 调用流式方法并收集所有内容
        for chunk in self.chat_stream(messages, system_prompt, temperature):
            full_response += chunk  # 拼接所有文本块
        
        return full_response  # 返回完整的响应文本


def main():
    """主函数，演示如何使用 OllamaClient 类"""
    
    print("="*60)
    print("Ollama 离线大模型调用示例")
    print("="*60)
    
    # 创建 Ollama 客户端实例
    client = OllamaClient(
        base_url="http://localhost:11434",  # Ollama 服务地址
        model="qwen2.5:7b"                   # 使用的模型
    )
    
    # 构建对话消息列表（模拟多轮对话）
    messages = [
        {"role": "user", "content": "写一首唐诗"},           # 第一轮用户输入
        {"role": "assistant", "content": "好的，我来为您创作"},  # AI 的回复
        {"role": "user", "content": "请再给我写一首边塞诗"},   # 第二轮用户输入
    ]
    
    # 设置系统提示词
    system_prompt = "你是一个著名的边塞诗人，擅长创作气势磅礴的边塞诗"
    
    print("\n正在生成回答（流式输出）...\n")
    print("-"*60)
    
    try:
        # 使用流式方法获取响应
        for chunk in client.chat_stream(messages, system_prompt):
            print(chunk, end="", flush=True)  # 逐块打印，实时显示
        
        print("\n" + "-"*60)
        print("\n[OK] 流式输出完成！\n")
        
        print("正在生成回答（非流式输出）...\n")
        print("-"*60)
        
        # 使用非流式方法获取完整响应
        response = client.chat(messages, system_prompt)
        print(response)  # 一次性打印完整内容
        
        print("-"*60)
        print("\n[OK] 非流式输出完成！")
        
    except Exception as e:
        # 捕获并打印异常信息
        print(f"\n[ERROR] 错误: {e}")
        print("\n[HELP] 请检查:")
        print("  1. Ollama 服务是否已启动 (ollama serve)")
        print("  2. 模型是否已安装 (ollama list)")
        print("  3. 网络连接是否正常")


if __name__ == "__main__":
    # 当脚本被直接运行时执行主函数
    main()
