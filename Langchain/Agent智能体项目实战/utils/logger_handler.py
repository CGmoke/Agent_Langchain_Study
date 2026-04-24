"""
项目日志
"""
import logging
from streamlit.logger import DEFAULT_LOG_MESSAGE
from utils.path_tool import get_abs_path
import os
from datetime import datetime
#获取日志保存的根目录
LOG_ROOT = get_abs_path("logs")

#创建日志文件
os.makedirs(LOG_ROOT,exist_ok=True)
#日志格式配置
DEFAULT_LOG_FORMAT  =logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - [%(name)s] - %(filename)s:%(lineno)d - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

#构建日志
def get_logger(
        name: str = "agent",
        console_level: int =logging.INFO,
        file_level: int =logging.DEBUG,
        log_file = None
)-> logging.Logger:
    """
    获取日志
    :param name: 日志名称
    :return: 日志对象
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    #避免重复添加处理器
    if logger.handlers:
        return logger
    #控制台处理器
    console_handler = logging.StreamHandler ()
    console_handler.setLevel(console_level)
    console_handler.setFormatter(DEFAULT_LOG_FORMAT)
    logger.addHandler(console_handler)

    #文件Handler
    if not log_file:
        log_file = os.path.join(LOG_ROOT,f"{name}_{datetime.now().strftime('%Y-%m-%d')}.log")
    file_handler = logging.FileHandler(log_file,encoding="utf-8")
    file_handler.setLevel(file_level)
    file_handler.setFormatter(DEFAULT_LOG_FORMAT)
    logger.addHandler(file_handler)

    return  logger
#快捷获取日志管理器
logger = get_logger()
# # if __name__ == '__main__':
# #     logger.info("测试日志")
# #     logger.error("测试错误日志")
# #     logger.debug("测试debug日志")
# #     logger.warning("测试警告日志")