from typing import Callable
from langchain.agents import AgentState
from langchain.agents.middleware import wrap_tool_call, before_model, dynamic_prompt, ModelRequest
from langchain.tools.tool_node import ToolCallRequest
from langchain_core.messages import ToolMessage
from langgraph.runtime import Runtime
from langgraph.types import Command
from tenacity import before
from utils.logger_handler import logger
from utils.prompt_loader import load_report_prompts,load_system_prompts
@wrap_tool_call
def monitor_tool(
        #请求数据封装
        request: ToolCallRequest,
        #执行函数本身
        handler: Callable[[ToolCallRequest],ToolMessage |Command],
)-> ToolMessage | Command: #监控工具
    logger.info(f"[tool monitor]执行工具:{request.tool_call['name']} ")
    logger.info(f"[tool monitor]工具参数:{request.tool_call['args']} ")
    try:
        result = handler(request)
        logger.info(f"[tool monitor]工具结果:{request.tool_call['name']}调用成功 ")
        if request.tool_call["name"] == "fill_context_for_report":
            request.runtime.context['report'] = True
        return result
    except Exception as e:
        logger.error(f"[tool monitor]工具执行失败:{str(e)} ")
        raise e



@before_model
def log_before_model(
        state: AgentState,#整个agent状态对象记录
        runtime: Runtime    #记录了整个执行过程中的上下文信息
):     #在模型执行前输出日志

    logger.info(f"[log_before_model]即将调用模型:带有{len(state['messages'])}条消息。 ")
    logger.debug(f"[log_before_model]当前消息:{type(state['messages'][-1]).__name__}|{state['messages'][-1].content.strip()} ")
    return None

@dynamic_prompt  #每一次在生成提示词之前调用此函数
def report_prompt_switch(request: ModelRequest):  #动态切换提示词
    is_report = request.runtime.context.get('report',False)
    if is_report:       #是否是生成报告,返回报告生成提示词内容
        return load_report_prompts()
    return load_system_prompts()