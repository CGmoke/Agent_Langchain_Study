import os
import random
from langchain_core.tools import tool
from rag.rag_service import RagSummaryService
from utils.logger_handler import logger
from agent.tools.weather_service import get_weather_info
from utils.config_handler import agent_conf
from utils.path_tool import get_abs_path
user_ids =  ['1001','1002','1003','1004','1005','1006','1007','1008','1009','1010']
month_arr=['2025-01','2025-02','2025-03','2025-04','2025-05','2025-06','2025-07','2025-08','2025-09','2025-10','2025-11','2025-12']
user_usages = {}
@tool (description="从向量库中检索参考资料")
def rag_summarize(query: str) -> str:
    """
    RAG总结
    :param query:
    :return:
    """
    rag = RagSummaryService()
    return rag.rag_summarize(query)
@tool (description="获取天气")
def get_weather(city: str)-> str:
    """
    获取天气
    :param city:
    :return:
    """
    return get_weather_info(city)

@tool(description="获取用户所在城市的名称，以纯字符串形式返回")
def get_user_city() -> str:
    """
    获取用户所在城市的名称，以纯字符串形式返回
    :return:
    """
    return "上海"

@tool(description="获取用户ID以纯字符串形式返回")
def get_user_id() -> str:
    """
    获取用户ID以纯字符串形式返回
    :return:
    """
    return random.choice(user_ids)
@tool(description="获取当前月份,以纯字符串形式返回")
def get_month()->str:
    """
    获取当前月份
    :return:
    """
    return random.choice(month_arr)

def generate_user_usage_tool():
    """
    生成用户使用记录工具
    :return:
    """
    if not user_usages:
        user_usages_path=get_abs_path(agent_conf["user_usages_path"])
        if not os.path.exists(user_usages_path):
            raise FileNotFoundError(f"[generate_user_usage_tool]用户使用记录文件不存在：{user_usages_path}")
        with open(user_usages_path,"r",encoding="utf-8") as f:
            for line in f.readlines()[1:]:
                user_usage: list[str] = line.strip().split(',')
                user_id: str = user_usage[0].replace('"','')
                feature: str = user_usage[1].replace('"','')
                efficiency: str = user_usage[2].replace('"','')
                consumables: str = user_usage[3].replace('"','')
                comparison: str = user_usage[4].replace('"','')
                time: str = user_usage[5].replace('"','')
                if user_id not in user_usages:
                    user_usages[user_id]={}
                user_usages[user_id][time]={
                    "特征":feature,
                    "效率":efficiency,
                    "损耗":consumables,
                    "对比":comparison
                }


@tool(description="从外部系统中获取指定用户在指定月份的使用记录,以纯字符串形式返回")
def get_user_usage(user_id:str,month:str)->str:
    """
    从外部系统中获取用户的使用记录
    :return:
    """
    generate_user_usage_tool()
    try:
        return str(user_usages[user_id][month])
    except KeyError as e:
        logger.warning(f"[get_user_usage]用户使用记录不存在：{user_id}，{month}")

@tool(description="无入参，无返回值，调用后触发中间件自动为报告生成的场景动态注入上下文信息，为后续提示词切换提供上下文信息")
def fill_context_for_report():
    return "fill_context_for_report已调用"

#测试
# if __name__ == '__main__':
#     print(get_user_usage("1001","2025-01"))