import os
def get_qwen_api_key():
    """获取通义千问 API Key"""
    if "QWEN_API_KEY" not in os.environ:
        with open("api_key.txt", "r") as f:
            os.environ["QWEN_API_KEY"] = f.read().strip()
    return os.environ["QWEN_API_KEY"]

def set_qwen_api_key():
    """设置通义千问 API Key 到环境变量"""
    api_key = get_qwen_api_key()
    os.environ["QWEN_API_KEY"] = api_key
    return api_key
