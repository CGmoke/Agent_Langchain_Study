# 🚀 基于黑马程序员学习视频整理的Rag与Agent学习与实战项目

> **从零到一的 LangChain 完整学习路径，涵盖 RAG 检索增强生成、Agent 智能体、提示词工程、链式编排等核心技术**

---

## 📖 项目简介

本项目是一个**系统性的 LangChain 框架学习与实战仓库**，包含 **4 大模块、40+ 个示例代码和 2 个完整项目**。通过循序渐进的学习路径，帮助开发者从零掌握 LangChain 核心技术，并具备构建生产级 AI 应用的能力。

### 🎯 项目定位

- **学习者**：系统学习 LangChain 框架的核心概念和最佳实践
- **开发者**：快速上手构建 RAG、Agent 等 AI 应用
- **研究者**：深入理解检索增强生成、智能体推理等技术原理

### ✨ 核心特性

| 特性 | 说明 |
|------|------|
| 🔥 **多模型支持** | 通义千问（云端）+ Ollama（本地离线）双模式 |
| 📚 **完整教程** | 40+ 个示例代码，覆盖 LangChain 全栈技术 |
| 🎯 **实战项目** | 2 个生产级完整项目（RAG客服 + Agent智能体） |
| 💬 **对话系统** | 多轮对话、流式输出、会话记忆完整实现 |
| 🔍 **RAG 技术** | 文档加载、向量存储、检索增强生成全流程 |
| 🤖 **Agent 智能体** | ReAct 推理、工具调用、中间件机制 |
| 🌐 **Web 界面** | Streamlit 构建的友好交互界面 |
| 📦 **开箱即用** | 完整的环境配置和依赖管理 |

---

## 🏗️ 项目架构

```
Langchain/
├── 📘 RAG基础/                    # RAG 技术基础教程（26课）
│   ├── 01-18课/                   # LangChain 核心概念入门
│   │   ├── 模型调用与流式输出
│   │   ├── 提示词工程
│   │   ├── 链式编排
│   │   ├── 输出解析器
│   │   └── 会话记忆管理
│   └── 19-26课/                   # RAG 核心技术
│       ├── 文档加载器（CSV/JSON/TXT/PDF）
│       ├── 文本分割器
│       ├── 向量存储与检索
│       └── 完整 RAG 链路实现
│
├── 🛒 RAG项目实战/                 # 生产级 RAG 项目
│   ├── 智能客服问答系统
│   ├── 知识库管理平台
│   ├── 多轮对话记忆
│   └── Web 界面（Streamlit）
│
├── 🤖 Agent智能体基础/              # Agent 基础教程（4课）
│   ├── Agent 初体验
│   ├── 流式输出
│   ├── ReAct 推理框架
│   └── 中间件机制
│
└── 🎯 Agent智能体项目实战/          # 生产级 Agent 项目
    ├── 扫地机器人智能客服
    ├── RAG + Agent 融合
    ├── 多工具协同
    ├── 天气查询服务
    └── 用户报告生成
```

---

## 📂 模块详解

### 1️⃣ RAG基础 - LangChain 核心技术教程

**位置**: `RAG基础/`  
**课程数量**: 26 课  
**学习时长**: 约 20 小时

#### 📋 课程大纲

| 阶段 | 课程 | 核心内容 |
|------|------|---------|
| **基础篇** | 01-06 | OpenAI 库使用、通义千问集成、Ollama 本地模型、流式输出 |
| **提示词篇** | 07-12 | 消息格式、PromptTemplate、FewShot、ChatPromptTemplate |
| **链式编排篇** | 13-16 | Chain 基础、输出解析器（JSON/Str）、RunnableLambda |
| **记忆篇** | 17-18 | 临时会话记忆、长期会话记忆 |
| **RAG篇** | 19-26 | 文档加载、文本分割、向量存储、检索增强生成 |

#### 🔑 核心文件说明

| 文件 | 功能 | 关键技术 |
|------|------|---------|
| `01Openai库的基本使用.py` | OpenAI API 调用 | API 调用、参数配置 |
| `05Langchain调用聊天模型.py` | 聊天模型集成 | ChatTongyi、消息格式 |
| `09langchain通用提示词.py` | 提示词模板 | PromptTemplate |
| `13chain的基础使用.py` | 链式编排 | LCEL 语法 |
| `17Memory临时会话记忆.py` | 会话管理 | ChatMessageHistory |
| `21TextLoader和文档分割器.py` | 文档处理 | TextLoader、RecursiveCharacterTextSplitter |
| `24外部向量持久化存储.py` | 向量数据库 | ChromaDB、持久化 |
| `26RunnnablePassthrough.py` | RAG 完整实现 | RunnablePassthrough、Retriever |

#### 🎯 学习目标

- ✅ 掌握 LangChain 核心概念（Runnable、Chain、Prompt）
- ✅ 理解提示词工程最佳实践
- ✅ 实现多轮对话和会话记忆
- ✅ 构建完整的 RAG 检索增强生成系统

---

### 2️⃣ RAG项目实战 - 生产级智能客服系统

**位置**: `RAG项目实战/`  
**应用场景**: 线上服装购买智能客服

#### 🌟 项目特性

- **智能问答**: 基于知识库的精准问答
- **多轮对话**: 支持上下文记忆的连续对话
- **知识库管理**: Web 界面上传文档，自动向量化
- **持久化存储**: ChromaDB 向量数据库 + 会话历史

#### 📁 项目结构

```
RAG项目实战/
├── Rag.py                    # RAG 服务核心类
├── vector_stores.py          # 向量存储服务
├── knowledge_base.py         # 知识库管理服务
├── file_history_store.py     # 会话历史管理
├── config_data.py            # 全局配置
├── app_qa.py                 # 智能客服问答界面
├── app_file_uploader.py      # 知识库文档上传界面
├── data/                     # 示例知识库文档
│   ├── 尺码推荐.txt
│   ├── 洗涤养护.txt
│   └── 颜色选择.txt
├── chroma_db/                # 向量数据库
└── chat_history/             # 会话历史记录
```

#### 🎬 快速启动

```bash
# 启动智能客服问答界面
streamlit run app_qa.py

# 启动知识库管理界面
streamlit run app_file_uploader.py
```

#### 📊 系统架构

```
用户 → Streamlit 界面 → RagService → VectorStoreService → ChromaDB
                              ↓
                         ChatTongyi (通义千问)
                              ↓
                         DashScopeEmbeddings
```

---

### 3️⃣ Agent智能体基础 - ReAct 推理框架教程

**位置**: `Agent智能体基础/`  
**课程数量**: 4 课  
**学习时长**: 约 4 小时

#### 📋 课程大纲

| 课程 | 文件 | 核心内容 |
|------|------|---------|
| 第1课 | `01Agent智能体初体验.py` | Agent 基本概念、工具定义、智能体创建 |
| 第2课 | `02Agent的stream流式输出.py` | 流式输出、实时响应、用户体验优化 |
| 第3课 | `03RaAct案例.py` | ReAct 推理框架、思考-行动-观察循环 |
| 第4课 | `04middleware中间件.py` | 中间件机制、提示词切换、上下文注入 |

#### 🔑 核心概念

**ReAct 框架**（Reasoning and Acting）:
```
思考（Reasoning）→ 行动（Acting）→ 观察（Observation）→ 再思考
```

**示例代码**:
```python
from langchain.agents import create_agent
from langchain_core.tools import tool

@tool(description="获取天气信息")
def get_weather(city: str) -> str:
    return f"{city}今天天气晴朗"

agent = create_agent(
    model=ChatTongyi(model="qwen3-max"),
    tools=[get_weather],
    system_prompt="你是智能助手，遵循ReAct框架"
)

# 流式执行
for chunk in agent.stream({"messages": [{"role": "user", "content": "北京天气如何？"}]}):
    print(chunk)
```

---

### 4️⃣ Agent智能体项目实战 - 扫地机器人智能客服

**位置**: `Agent智能体项目实战/`  
**应用场景**: 扫地机器人专业智能客服

#### 🌟 项目特性

- **ReAct 智能体**: 自主思考与工具调用
- **RAG 检索**: 从知识库检索专业资料
- **天气适配**: 实时天气查询，判断使用环境
- **用户报告**: 生成个性化使用报告
- **多工具协同**: 7 种专业工具智能调用

#### 🛠️ 工具集

| 工具 | 功能 | 参数 |
|------|------|------|
| `rag_summarize` | 从向量库检索专业资料 | query: 检索词 |
| `get_weather` | 获取城市天气信息 | city: 城市名称 |
| `get_user_id` | 获取当前用户 ID | 无 |
| `get_user_city` | 获取用户所在城市 | 无 |
| `get_month` | 获取当前月份 | 无 |
| `get_user_usage` | 查询用户使用记录 | user_id, month |
| `fill_context_for_report` | 报告生成上下文注入 | 无 |

#### 📁 项目结构

```
Agent智能体项目实战/
├── agent/
│   ├── react_agent.py           # ReAct 智能体实现
│   └── tools/
│       ├── agent_tools.py       # Agent 工具定义
│       ├── weather_service.py   # 天气查询服务
│       └── middleware.py        # 中间件
├── rag/
│   ├── rag_service.py           # RAG 服务
│   └── vector_store.py          # 向量存储服务
├── model/
│   └── factory.py               # 模型工厂
├── utils/
│   ├── config_handler.py        # 配置管理
│   ├── logger_handler.py        # 日志处理
│   └── path_tool.py             # 路径工具
├── config/                      # 配置文件（YAML）
├── data/                        # 知识库文档
├── prompts/                     # 提示词文件
├── app.py                       # Streamlit 应用入口
└── .env                         # 环境变量配置
```

#### 🎬 快速启动

```bash
# 配置环境变量
cp .env.example .env
# 编辑 .env 文件，填入 API Key

# 启动 Web 应用
streamlit run app.py
```

#### 💬 使用示例

```
用户: 小户型如何使用扫地机器人？
系统: [调用 rag_summarize 工具] → 返回专业建议

用户: 今天北京天气怎么样，适合用扫地机器人吗？
系统: [调用 get_weather 工具] → 返回天气信息和使用建议

用户: 给我生成我的使用报告
系统: [依次调用 get_user_id → get_month → fill_context_for_report → get_user_usage] → 生成报告
```

---

## 🛠️ 技术栈

### 核心依赖

| 类别 | 技术 | 版本 | 用途 |
|------|------|------|------|
| **语言** | Python | 3.8+ | 编程语言 |
| **框架** | langchain-core | Latest | LangChain 核心框架 |
| | langchain-community | Latest | 社区集成组件 |
| | langchain-openai | Latest | OpenAI 兼容接口 |
| | langchain-chroma | Latest | ChromaDB 集成 |
| **模型** | 通义千问 | qwen3-max | 云端大模型 |
| | DashScope | text-embedding-v4 | 文本嵌入模型 |
| | Ollama | qwen2.5:7b | 本地离线模型 |
| **向量数据库** | ChromaDB | Latest | 持久化向量存储 |
| **Web 框架** | Streamlit | Latest | Web 界面构建 |
| **工具** | SerpApi | Latest | 天气查询服务 |

### 外部服务

| 服务 | 说明 | 获取方式 |
|------|------|---------|
| 阿里云通义千问 | 云端大模型服务 | [DashScope 控制台](https://dashscope.console.aliyun.com/) |
| Ollama | 本地模型运行时 | [Ollama 官网](https://ollama.ai/) |
| SerpApi | 搜索引擎 API | [SerpApi 官网](https://serpapi.com/) |

---

## 🚀 快速开始

### 环境要求

- **操作系统**: Windows / macOS / Linux
- **Python 版本**: 3.8 或更高版本
- **内存要求**: 
  - 仅云端模型: ≥ 4GB RAM
  - 本地模型: ≥ 16GB RAM（推荐 32GB）

### 安装步骤

#### 1. 克隆项目

```bash
git clone <repository-url>
cd Langchain
```

#### 2. 创建虚拟环境

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

#### 3. 安装依赖

```bash
# 核心依赖
pip install langchain langchain-core langchain-community
pip install langchain-openai langchain-chroma langchain-text-splitters

# 模型相关
pip install dashscope

# Web 框架
pip install streamlit

# 工具库
pip install python-dotenv google-search-results

# 可选：本地模型支持
pip install langchain-ollama
```

#### 4. 配置 API Key

**方式一：环境变量（推荐）**

创建 `.env` 文件：
```env
LLM_API_KEY="your-qwen-api-key"
LLM_MODEL_ID="qwen3-max"
LLM_BASE_URL="https://dashscope.aliyuncs.com/compatible-mode/v1"
SERPAPI_API_KEY="your-serpapi-key"
```

**方式二：配置文件**

在项目根目录创建 `api_key.txt`：
```
sk-your-qwen-api-key
```

**获取 API Key**:
- 通义千问: [阿里云 DashScope](https://dashscope.console.aliyun.com/)
- SerpApi: [SerpApi 官网](https://serpapi.com/)

#### 5. （可选）安装 Ollama 本地模型

```bash
# 安装 Ollama
# 访问 https://ollama.ai/ 下载安装

# 下载模型
ollama pull qwen2.5:7b
```

---

## 📚 学习路径

### 🎯 推荐学习顺序

```
第1阶段：LangChain 基础（RAG基础/01-18课）
    ↓
第2阶段：RAG 技术深入（RAG基础/19-26课）
    ↓
第3阶段：RAG 项目实战（RAG项目实战/）
    ↓
第4阶段：Agent 基础（Agent智能体基础/）
    ↓
第5阶段：Agent 项目实战（Agent智能体项目实战/）
```

### 📖 详细学习计划

#### 第1周：LangChain 基础
- Day 1-2: 模型调用与流式输出（01-06课）
- Day 3-4: 提示词工程（07-12课）
- Day 5-6: 链式编排与输出解析（13-16课）
- Day 7: 会话记忆管理（17-18课）

#### 第2周：RAG 技术
- Day 1-2: 文档加载器（19-22课）
- Day 3-4: 向量存储与检索（23-24课）
- Day 5-6: RAG 完整实现（25-26课）
- Day 7: RAG 项目实战

#### 第3周：Agent 智能体
- Day 1-2: Agent 基础（01-02课）
- Day 3-4: ReAct 框架（03-04课）
- Day 5-7: Agent 项目实战

---

## 💡 使用示例

### 示例1：基础对话

```python
from langchain_community.chat_models import ChatTongyi

model = ChatTongyi(
    api_key="your-api-key",
    model="qwen3-max"
)

response = model.invoke("你好，介绍一下自己")
print(response.content)
```

### 示例2：RAG 检索增强生成

```python
from langchain_community.chat_models import ChatTongyi
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

# 初始化模型和向量存储
model = ChatTongyi(api_key="your-key", model="qwen3-max")
embeddings = DashScopeEmbeddings(model="text-embedding-v4", dashscope_api_key="your-key")
vector_store = Chroma(embedding_function=embeddings, persist_directory="./chroma_db")

# 构建 RAG 链
prompt = ChatPromptTemplate.from_messages([
    ("system", "基于参考资料回答：{context}"),
    ("human", "{input}")
])

retriever = vector_store.as_retriever(search_kwargs={"k": 3})
chain = (
    {"input": RunnablePassthrough(), "context": retriever}
    | prompt
    | model
)

response = chain.invoke("如何使用扫地机器人？")
print(response.content)
```

### 示例3：Agent 工具调用

```python
from langchain.agents import create_agent
from langchain_core.tools import tool

@tool(description="计算BMI指数")
def calculate_bmi(weight: float, height: float) -> str:
    bmi = weight / (height ** 2)
    return f"BMI指数为: {bmi:.2f}"

agent = create_agent(
    model=ChatTongyi(model="qwen3-max"),
    tools=[calculate_bmi],
    system_prompt="你是健康助手"
)

for chunk in agent.stream({"messages": [{"role": "user", "content": "我70kg，1.75m，计算BMI"}]}):
    print(chunk)
```

---

## 📊 项目对比

| 特性 | RAG基础 | RAG项目实战 | Agent基础 | Agent项目实战 |
|------|---------|------------|-----------|--------------|
| **类型** | 教程 | 完整项目 | 教程 | 完整项目 |
| **代码量** | 26个示例 | 完整系统 | 4个示例 | 完整系统 |
| **Web界面** | ❌ | ✅ Streamlit | ❌ | ✅ Streamlit |
| **向量数据库** | ✅ | ✅ ChromaDB | ❌ | ✅ ChromaDB |
| **会话记忆** | ✅ | ✅ 持久化 | ❌ | ✅ |
| **工具调用** | ❌ | ❌ | ✅ | ✅ 7种工具 |
| **ReAct推理** | ❌ | ❌ | ✅ | ✅ |
| **生产级** | ❌ | ✅ | ❌ | ✅ |

---

## 🔧 常见问题

### Q1: 如何选择云端模型还是本地模型？

**A**: 
- **云端模型（推荐）**: 通义千问等，性能强大，无需本地资源
- **本地模型**: Ollama，隐私性好，但需要较高硬件配置

### Q2: 向量数据库如何选择？

**A**:
- **开发测试**: InMemoryVectorStore（内存存储）
- **生产环境**: ChromaDB（持久化存储，支持大规模数据）

### Q3: 如何调试 LangChain 应用？

**A**:
```python
# 设置调试模式
import langchain
langchain.debug = True

# 或使用 set_debug
from langchain.globals import set_debug
set_debug(True)
```

### Q4: API Key 如何安全管理？

**A**:
1. 使用 `.env` 文件（不提交到 Git）
2. 使用环境变量
3. 使用密钥管理服务（生产环境）

### Q5: 如何提升 RAG 检索效果？

**A**:
1. 优化文本分割参数（chunk_size, chunk_overlap）
2. 调整检索数量（k值）
3. 使用混合检索（向量+关键词）
4. 优化提示词模板

### Q6: Agent 工具调用失败怎么办？

**A**:
1. 检查工具描述是否清晰
2. 确认参数类型和格式
3. 查看日志输出
4. 使用 `langchain.debug = True` 调试

---

## 🤝 贡献指南

### 提交规范

- `feat`: 新功能
- `fix`: 修复 Bug
- `docs`: 文档更新
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建/工具链更新

### 开发流程

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'feat: Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交 Pull Request

### 代码规范

- 遵循 PEP 8 编码规范
- 添加必要的注释和文档字符串
- 编写单元测试
- 更新相关文档

---

## 📝 更新日志

### v1.0.0 (2026-04-30)
- ✨ 完成 RAG 基础教程（26课）
- ✨ 完成 Agent 智能体基础教程（4课）
- ✨ 完成 RAG 项目实战
- ✨ 完成 Agent 项目实战
- 📝 完善项目文档

---

## 📄 许可证

本项目仅供学习和研究使用。

---

## 📞 联系方式

如有问题或建议，请提交 Issue 或 Pull Request。

---

## 🙏 致谢

- [LangChain](https://www.langchain.com/) - 强大的 LLM 应用开发框架
- [通义千问](https://tongyi.aliyun.com/) - 阿里云大语言模型
- [Streamlit](https://streamlit.io/) - 快速构建数据应用
- [ChromaDB](https://www.trychroma.com/) - 开源向量数据库
- [Ollama](https://ollama.ai/) - 本地大模型运行时
- [SerpApi](https://serpapi.com/) - 搜索引擎 API 服务

---

**⭐ 如果这个项目对你有帮助，请给一个 Star ⭐**

