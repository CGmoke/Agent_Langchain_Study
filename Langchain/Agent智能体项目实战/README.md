# 智扫通机器人智能客服系统

基于 LangChain + 通义千问的智能客服 Agent 项目，集成 RAG 检索增强生成、天气查询、用户使用报告生成等功能。

## 项目概述

本项目是一个面向扫地机器人和扫拖一体机器人的专业智能客服系统，采用 ReAct（Reasoning and Acting）架构，具备自主思考与工具调用能力。系统能够根据用户问题智能判断并调用相应工具，提供专业的产品咨询、故障排查、使用建议和个性化报告服务。

### 核心特性

- **智能对话**：基于通义千问大模型，提供流畅自然的对话体验
- **RAG 检索**：从知识库中精准检索专业资料，提供权威解答
- **天气适配**：实时查询天气信息，判断环境是否适合使用机器人
- **用户报告**：生成个性化的机器人使用报告和数据分析
- **工具调用**：自主判断并调用多种工具，实现复杂任务自动化
- **Web 界面**：基于 Streamlit 的友好交互界面

## 技术架构

### 技术栈

| 类别 | 技术选型 |
|------|----------|
| 大语言模型 | 通义千问（Qwen3-max） |
| 框架 | LangChain |
| 向量数据库 | ChromaDB |
| 文本嵌入 | DashScope Embeddings |
| Web 框架 | Streamlit |
| 天气服务 | SerpApi |
| 配置管理 | YAML |
| 日志系统 | Python logging |

### 系统架构图

```
┌─────────────────────────────────────────────────────────┐
│                    Streamlit Web 界面                    │
│                      (app.py)                           │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                  ReAct Agent 智能体                      │
│                (react_agent.py)                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │  思考 → 行动 → 观察 → 再思考                       │  │
│  └──────────────────────────────────────────────────┘  │
└──────────┬──────────────────────────────────────────────┘
           │
           ├──────────────┬──────────────┬─────────────────┐
           ▼              ▼              ▼                 ▼
    ┌──────────┐   ┌──────────┐   ┌──────────┐    ┌────────────┐
    │ RAG 服务  │   │ 天气查询  │   │ 用户记录  │    │ 报告生成   │
    │          │   │          │   │          │    │            │
    └─────┬────┘   └─────┬────┘   └─────┬────┘    └──────┬─────┘
          │              │              │                 │
          ▼              ▼              ▼                 ▼
    ┌──────────┐   ┌──────────┐   ┌──────────┐    ┌────────────┐
    │ChromaDB  │   │ SerpApi  │   │   CSV    │    │ 通义千问   │
    │向量数据库 │   │ 天气API  │   │ 数据文件 │    │   大模型   │
    └──────────┘   └──────────┘   └──────────┘    └────────────┘
```

## 项目结构

```
Agent智能体项目实战/
├── agent/                    # Agent 核心模块
│   ├── react_agent.py       # ReAct 智能体实现
│   └── tools/               # 工具集
│       ├── agent_tools.py   # Agent 工具定义
│       ├── weather_service.py # 天气查询服务
│       └── middleware.py    # 中间件
├── rag/                     # RAG 检索模块
│   ├── rag_service.py       # RAG 服务
│   └── vector_store.py      # 向量存储服务
├── model/                   # 模型工厂
│   └── factory.py           # 模型实例化工厂
├── utils/                   # 工具类
│   ├── config_handler.py    # 配置管理
│   ├── logger_handler.py    # 日志处理
│   ├── path_tool.py         # 路径工具
│   ├── file_handler.py      # 文件处理
│   └── prompt_loader.py     # 提示词加载
├── config/                  # 配置文件
│   ├── agent.yml            # Agent 配置
│   ├── rag.yml              # RAG 配置
│   ├── chroma.yml           # 向量库配置
│   └── prompts.yml          # 提示词配置
├── data/                    # 数据文件
│   ├── 扫地机器人100问.pdf
│   ├── 扫地机器人100问2.txt
│   ├── 扫拖一体机器人100问.txt
│   ├── 故障排除.txt
│   ├── 维护保养.txt
│   ├── 选购指南.txt
│   └── external/
│       └── records.csv      # 用户使用记录
├── prompts/                 # 提示词文件
│   ├── main_prompt.txt      # 主提示词
│   ├── rag_summarize_prompt.txt
│   └── report_prompt.txt
├── logs/                    # 日志目录
├── app.py                   # Streamlit 应用入口
├── .env                     # 环境变量配置
└── README.md                # 项目文档
```

## 核心功能模块

### 1. ReAct 智能体

基于 LangChain 的 ReAct（Reasoning and Acting）架构，实现"思考→行动→观察→再思考"的循环推理过程。

**核心能力**：
- 自主判断用户意图
- 智能选择并调用工具
- 多轮工具调用完成复杂任务
- 流式输出响应结果

**示例代码**：
```python
from agent.react_agent import ReactAgent

agent = ReactAgent()
for chunk in agent.executive_stream("小户型如何使用扫地机器人？"):
    print(chunk, end="", flush=True)
```

### 2. RAG 检索增强生成

从向量数据库中检索相关专业知识，结合大模型生成专业回答。

**核心能力**：
- 文档自动分片与向量化
- MD5 去重机制
- 语义相似度检索
- 上下文增强生成

**支持文档格式**：
- PDF 文件
- TXT 文本文件

**示例代码**：
```python
from rag.rag_service import RagSummaryService

rag = RagSummaryService()
result = rag.rag_summarize("扫地机器人如何维护保养？")
print(result)
```

### 3. 工具集

系统提供多种工具供 Agent 调用：

| 工具名称 | 功能描述 | 参数 |
|---------|---------|------|
| `rag_summarize` | 从向量库检索专业资料 | query: 检索词 |
| `get_weather` | 获取城市天气信息 | city: 城市名称 |
| `get_user_id` | 获取当前用户 ID | 无 |
| `get_user_city` | 获取用户所在城市 | 无 |
| `get_month` | 获取当前月份 | 无 |
| `get_user_usage` | 查询用户使用记录 | user_id, month |
| `fill_context_for_report` | 报告生成上下文注入 | 无 |

### 4. 天气查询服务

基于 SerpApi 实现实时天气查询，判断环境是否适合使用机器人。

**示例代码**：
```python
from agent.tools.weather_service import get_weather_info

weather = get_weather_info("北京")
print(weather)
```

## 环境配置

### 前置要求

- Python 3.10+
- pip 包管理器

### 安装步骤

1. **克隆项目**
```bash
git clone <repository-url>
cd Agent智能体项目实战
```

2. **创建虚拟环境**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **安装依赖**
```bash
pip install langchain langchain-community langchain-chroma
pip install langchain-text-splitters
pip install streamlit
pip install python-dotenv
pip install google-search-results
pip install dashscope
```

4. **配置环境变量**

创建 `.env` 文件并配置以下内容：
```env
LLM_API_KEY="your-qwen-api-key"
LLM_MODEL_ID="qwen3-max"
LLM_BASE_URL="https://dashscope.aliyuncs.com/compatible-mode/v1"
SERPAPI_API_KEY="your-serpapi-key"
```

**获取 API Key**：
- 通义千问 API Key：[阿里云 DashScope](https://dashscope.console.aliyun.com/)
- SerpApi Key：[SerpApi 官网](https://serpapi.com/)

5. **准备知识库数据**

将扫地机器人相关文档放入 `data/` 目录，支持格式：
- PDF 文件
- TXT 文本文件

## 使用指南

### 启动 Web 应用

```bash
streamlit run app.py
```

应用将在浏览器中打开，默认地址：`http://localhost:8501`

### 使用示例

#### 1. 产品咨询
```
用户：小户型如何使用扫地机器人？
系统：调用 rag_summarize 工具检索专业知识，生成详细建议
```

#### 2. 天气适配咨询
```
用户：今天北京天气怎么样，适合用扫地机器人吗？
系统：调用 get_weather 工具查询天气，给出使用建议
```

#### 3. 生成使用报告
```
用户：给我生成我的使用报告
系统：依次调用 get_user_id → get_month → fill_context_for_report → get_user_usage，生成个性化报告
```

### 加载知识库

首次运行前，需要加载知识库数据：

```python
from rag.vector_store import VectorStoreService

vector_store = VectorStoreService()
vector_store.load_document()
```

## 配置说明

### Agent 配置（config/agent.yml）

```yaml
user_usages_path: data/external/records.csv
```

### RAG 配置（config/rag.yml）

```yaml
chat_model_name: qwen3-max          # 聊天模型名称
embedding_model_name: text-embedding-v4  # 嵌入模型名称
```

### 向量库配置（config/chroma.yml）

```yaml
collection_name: agent              # 集合名称
persist_directory: chorma_db        # 持久化目录
k: 3                                # 检索返回文档数
data_path: data                     # 数据目录
md5_hex_store: md5.txt              # MD5 记录文件
allow_konwledge_file_type: [pdf, txt]  # 允许的文件类型
chunk_size: 200                     # 文档分片大小
chunk_overlap: 20                   # 分片重叠大小
separators: ["\n\n", "\n", ".", ",", "!", "?", "。", "！", "？"]
```

## API 文档

### ReActAgent 类

**初始化**
```python
agent = ReactAgent()
```

**执行查询（流式输出）**
```python
def executive_stream(self, query: str) -> Generator[str, None, None]:
    """
    流式执行用户查询
    
    参数:
        query: 用户问题
    
    返回:
        生成器，每次 yield 一个文本片段
    """
```

### VectorStoreService 类

**初始化**
```python
vector_store = VectorStoreService()
```

**加载文档**
```python
def load_document(self, file_path: str = None) -> None:
    """
    从数据文件夹读取文档并存入向量库
    
    参数:
        file_path: 文件路径（可选，默认使用配置文件中的路径）
    """
```

**获取检索器**
```python
def get_retriever(self) -> VectorStoreRetriever:
    """
    获取向量检索器
    
    返回:
        VectorStoreRetriever 对象
    """
```

### RagSummaryService 类

**RAG 总结**
```python
def rag_summarize(self, query: str) -> str:
    """
    基于检索增强生成回答
    
    参数:
        query: 用户问题
    
    返回:
        生成的回答文本
    """
```

## 常见问题解答（FAQ）

### Q1: 如何获取通义千问 API Key？

**A**: 访问[阿里云 DashScope 控制台](https://dashscope.console.aliyun.com/)，注册账号后即可获取 API Key。

### Q2: SerpApi 天气查询失败怎么办？

**A**: 检查以下几点：
1. 确认 `.env` 文件中 `SERPAPI_API_KEY` 配置正确
2. 检查 API Key 是否有效且有剩余配额
3. 确认网络连接正常

### Q3: 知识库文档加载失败？

**A**: 常见原因：
1. 文件编码问题：确保 TXT 文件为 UTF-8 编码
2. 文件路径错误：检查 `config/chroma.yml` 中的 `data_path` 配置
3. 文件格式不支持：仅支持 PDF 和 TXT 格式

### Q4: 如何添加新的知识文档？

**A**: 将文档放入 `data/` 目录，然后运行：
```python
from rag.vector_store import VectorStoreService
vector_store = VectorStoreService()
vector_store.load_document()
```

### Q5: 如何自定义提示词？

**A**: 修改 `prompts/main_prompt.txt` 文件，按照现有格式调整提示词内容。

### Q6: 向量数据库存储在哪里？

**A**: 默认存储在 `chorma_db/` 目录，可在 `config/chroma.yml` 中修改 `persist_directory` 配置。

## 开发指南

### 添加新工具

1. 在 `agent/tools/agent_tools.py` 中定义工具函数：
```python
@tool(description="工具描述")
def new_tool(param: str) -> str:
    """工具功能说明"""
    # 实现逻辑
    return result
```

2. 在 `agent/react_agent.py` 的工具列表中添加：
```python
tools=[..., new_tool]
```

### 扩展中间件

在 `agent/tools/middleware.py` 中添加新的中间件函数：
```python
def custom_middleware(agent, input_dict, context):
    # 中间件逻辑
    return input_dict
```

### 日志查看

日志文件位于 `logs/` 目录，按日期命名：
```
logs/agent_2026-04-30.log
```

## 性能优化建议

1. **向量检索优化**：调整 `chunk_size` 和 `k` 参数平衡检索精度和速度
2. **模型选择**：根据需求选择合适的模型，`qwen-turbo` 速度更快，`qwen3-max` 效果更好
3. **缓存机制**：对频繁查询的问题实现缓存
4. **并发处理**：使用异步处理提升并发能力

## 安全注意事项

1. **API Key 保护**：不要将 `.env` 文件提交到版本控制系统
2. **用户数据**：用户使用记录包含敏感信息，注意数据脱敏
3. **输入验证**：对用户输入进行验证，防止注入攻击

## 贡献指南

### 提交规范

- `feat`: 新功能
- `fix`: 修复 Bug
- `docs`: 文档更新
- `refactor`: 代码重构
- `test`: 测试相关

### 开发流程

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'feat: Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交 Pull Request

## 许可证

本项目仅供学习和研究使用。

## 联系方式

如有问题或建议，请提交 Issue 或 Pull Request。

## 致谢

- [LangChain](https://www.langchain.com/) - 强大的 LLM 应用开发框架
- [通义千问](https://tongyi.aliyun.com/) - 阿里云大语言模型
- [Streamlit](https://streamlit.io/) - 快速构建数据应用
- [ChromaDB](https://www.trychroma.com/) - 开源向量数据库
- [SerpApi](https://serpapi.com/) - 搜索引擎 API 服务

---

**最后更新时间**: 2026-04-30
