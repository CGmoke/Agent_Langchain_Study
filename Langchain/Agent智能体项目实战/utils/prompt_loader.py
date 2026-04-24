from streamlit import rerun
from utils.config_handler import prompts_conf
from utils.path_tool import get_abs_path
from utils.logger_handler import logger

def load_system_prompts( ):
    try:
        system_prompt_path = get_abs_path(prompts_conf['main_prompt_path'])
    except KeyError as e:
        logger.error(f"[load_system_prompts]在yaml配置文件中没有main_prompt.txt的配置项")
        raise e
    try:
        return open(system_prompt_path, "r", encoding='utf-8').read()
    except Exception as e:
        logger.error(f"[load_system_prompts]在路径：{system_prompt_path}解析系统提示词失败，错误信息：{str(e)}")
        raise e

def load_rag_prompts( ):
    try:
        summarize_prompt_path = get_abs_path(prompts_conf['rag_summarize_prompt_path'])
    except KeyError as e:
        logger.error(f"[load_system_prompts]在yaml配置文件中没有main_prompt.txt的配置项")
        raise e
    try:
        return open(summarize_prompt_path, "r", encoding='utf-8').read()
    except Exception as e:
        logger.error(f"[load_system_prompts]在路径：{summarize_prompt_path}解析RAG总结提示词失败，错误信息：{str(e)}")
        raise e


def load_report_prompts( ):
    try:
        rag_prompt_path = get_abs_path(prompts_conf['report_prompt_path'])
    except KeyError as e:
        logger.error(f"[load_system_prompts]在yaml配置文件中没有main_prompt.txt的配置项")
        raise e
    try:
        return open(rag_prompt_path, "r", encoding= "utf-8").read()
    except Exception as e:
        logger.error(f"[load_system_prompts]在路径：{rag_prompt_path}解析report提示词失败，错误信息：{str(e)}")
        raise e

# if __name__ == '__main__':
#     print(load_system_prompts())
#     print(load_summarize_prompts())
#     print(load_report_prompts())