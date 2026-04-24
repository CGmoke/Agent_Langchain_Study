"""
天气查询服务 - 基于SerpApi实现
"""
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()


def load_serpapi_key() -> str:
    """
    加载 SerpApi API Key
    """
    env_key = os.getenv("SERPAPI_API_KEY")
    if env_key and env_key.strip():
        return env_key.strip()
    
    possible_paths = [
        "api_key_serpapi.txt",
        "../api_key_serpapi.txt",
        "../../api_key_serpapi.txt",
        os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "HelloAgent", "api_key_serpapi.txt"),
    ]
    
    for file_path in possible_paths:
        try:
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                    lines = [line.strip() for line in content.split('\n')
                             if line.strip() and not line.startswith('#')]
                    if lines:
                        key = lines[0]
                        if key and len(key) > 20:
                            return key
        except Exception:
            continue
    
    return ""


def get_weather_info(city: str) -> str:
    """
    获取指定城市的天气信息
    
    参数:
        city: 城市名称（如：北京、上海、新乡）
    
    返回:
        天气信息的字符串描述
    """
    api_key = load_serpapi_key()
    if not api_key:
        return "[ERROR] SERPAPI_API_KEY 未配置，请在 .env 文件或 api_key_serpapi.txt 中配置"
    
    try:
        from serpapi import GoogleSearch
        
        params = {
            'engine': 'google',
            'q': f'{city} weather',
            'api_key': api_key,
            'hl': 'zh-cn',
            'gl': 'cn',
        }
        
        search = GoogleSearch(params)
        results = search.get_dict()
        
        # 检查 API 错误响应
        if 'error' in results:
            return f"[ERROR] SerpApi 错误：{results['error']}"
        
        weather_result = results.get('weather_result', {})
        if not weather_result:
            weather_result = results.get('answer_box', {})

        if not weather_result:
            organic_results = results.get('organic_results', [])
            if organic_results:
                first_result = organic_results[0]
                snippet = first_result.get('snippet', '')
                if snippet:
                    return f"{city}天气信息：{snippet[:200]}"
        if weather_result:
            date = weather_result.get('date', '')
            temperature = weather_result.get('temperature', '')
            condition = weather_result.get('condition', '')
            humidity = weather_result.get('humidity', '')
            wind = weather_result.get('wind', '')

            weather_info = f"{city}天气："
            if date:
                weather_info += f"{date}，"
            if condition:
                weather_info += f"{condition}，"
            if temperature:
                weather_info += f"气温{temperature}"
            if humidity:
                weather_info += f"，湿度{humidity}"
            if wind:
                weather_info += f"，{wind}"

            if weather_info.endswith("：") or weather_info.endswith("，"):
                weather_info = weather_info.rstrip("，：")

            return weather_info if len(weather_info) > 10 else f"[WARNING] 未能获取到{city}的详细天气信息"
        else:
            return f"[WARNING] 未能获取到{city}的天气信息，请检查城市名称是否正确"

    except ImportError:
        return "[ERROR] 缺少依赖包，请运行：pip install google-search-results"
    except Exception as e:
        error_msg = str(e)
        if "Expecting value" in error_msg:
            return f"[ERROR] SerpApi 返回无效响应，可能是 API Key 无效或网络问题。请检查：1) API Key 是否正确 2) 网络连接是否正常 3) API 配额是否用尽"
        return f"[ERROR] 天气查询失败：{error_msg}"


if __name__ == '__main__':
    print(get_weather_info("北京"))
    print(get_weather_info("郑州"))
