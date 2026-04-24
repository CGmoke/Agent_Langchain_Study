from langchain.agents import create_agent
from model.factory import chat_model
from utils.prompt_loader import load_system_prompts
from agent.tools.agent_tools import (rag_summarize,get_weather,get_user_id,
                                     get_user_city,get_month,get_user_usage,generate_user_usage_tool,fill_context_for_report)
from agent.tools.middleware import monitor_tool,log_before_model,report_prompt_switch
class ReactAgent():
    """
    ReactAgent
    """
    def __init__(self):
        self.agent = create_agent(
            model = chat_model,
            system_prompt=load_system_prompts(),
            tools=[rag_summarize,get_weather,get_user_id,get_user_city,get_month,get_user_usage,
                   generate_user_usage_tool,fill_context_for_report],
            middleware=[monitor_tool,log_before_model,report_prompt_switch]
        )
    def executive_stream(self,query:str):
        input_dict = {
            "messages":[
                {
                    "role": "user",
                    "content": query
                }
            ]
        }
        #第三个参数context就是上下文runtime中的信息，就是做提示词切换的标记
        for chunk in self.agent.stream(input_dict,stream_mode="values",context={"report":False}):
            latest_message = chunk['messages'][-1]
            yield latest_message.content.strip() + "\n"

if __name__ == '__main__':
    agent = ReactAgent()
    for chunk in agent.executive_stream("给我生成我的使用报告"):
        print(chunk,end="",flush=True)
