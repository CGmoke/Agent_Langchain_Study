import os

def get_qwen_api_key():
    """获取通义千问 API Key"""
    if "QWEN_API_KEY" not in os.environ or not os.environ["QWEN_API_KEY"].strip():
        # 尝试多个可能的路径
        possible_paths = [
            "api_key.txt",                                    # 当前目录
            "../api_key.txt",                                 # 上级目录
            os.path.join(os.path.dirname(__file__), "api_key.txt"),  # 相对于本文件位置
        ]
        
        for file_path in possible_paths:
            try:
                if os.path.exists(file_path):
                    with open(file_path, "r", encoding="utf-8") as f:
                        key = f.read().strip()
                    if key:
                        os.environ["QWEN_API_KEY"] = key
                        return key
            except Exception as e:
                continue
        
        raise FileNotFoundError(
            "未找到 api_key.txt 文件。请确保在以下任一位置创建该文件:\n"
            "  - 当前目录: api_key.txt\n"
            "  - 项目根目录: api_key.txt\n"
            "  - qwen_api_key.py 同级目录: api_key.txt"
        )
    
    return os.environ["QWEN_API_KEY"]

def set_qwen_api_key():
    """设置通义千问 API Key 到环境变量"""
    api_key = get_qwen_api_key()
    os.environ["QWEN_API_KEY"] = api_key
    return api_key
