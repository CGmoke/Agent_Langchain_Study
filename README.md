# 🤖 Agent_Langchain_Study - LangChain 框架学习指南

> **从入门到精通的 LangChain 实战教程，涵盖大模型调用、提示词工程、链式编排、RAG 检索增强生成及记忆管理等核心技能**

---

## 📖 项目简介

本项目是一个**系统性学习 LangChain 框架的实战教程仓库**，包含 **26+ 个精心设计的示例代码**，覆盖了 LangChain 的核心概念和最佳实践。通过循序渐进的学习路径，帮助开发者快速掌握使用 LangChain 构建智能应用的关键技术。

### ✨ 核心特性

- 🔥 **多模型支持**: 同时支持云端大模型（通义千问）和本地离线模型（Ollama/Qwen2.5）
- 💬 **对话式交互**: 支持多轮对话、流式输出、消息格式化等完整对话功能
- 🎯 **提示词工程**: 深入讲解 PromptTemplate、ChatPromptTemplate、FewShotPromptTemplate 三大模板体系
- ⛓️ **链式编排**: 掌握 Chain 组合模式，构建复杂的 AI 应用流程
- 🔧 **输出解析**: 支持 JSON、字符串等多种格式的结构化输出解析
- 🧠 **会话记忆**: 实现基于内存的上下文保持和多轮对话管理
- 🔍 **RAG 检索增强**: 从零构建完整的 RAG 系统，包括文档加载、文本分割、向量存储、相似度检索
- 📚 **实战导向**: 每个示例都是可运行的独立脚本，即学即用

---

## 🛠️ 技术栈说明

### 核心依赖

| 技术 | 版本 | 用途 |
|------|------|------|
| **Python** | 3.8+ | 编程语言 |
| **langchain-core** | Latest | LangChain 核心框架（Runnable、Chain、Prompt） |
| **langchain-community** | Latest | 社区集成组件（文档加载器、嵌入模型） |
| **langchain-openai** | Latest | OpenAI 兼容接口 |
| **langchain_ollama** | Latest | Ollama 本地模型集成 |
| **langchain-chroma** | Latest | ChromaDB 向量数据库集成 |
| **langchain-text-splitters** | Latest | 文本分割器（RecursiveCharacterTextSplitter） |
| **通义千问 API** | DashScope | 云端大模型服务 + 文本嵌入模型 |
| **Ollama** | Latest | 本地大模型运行时 |
| **ChromaDB** | Latest | 持久化向量存储数据库 |

### 外部服务

| 服务 | 说明 |
|------|------|
| **阿里云通义千问** | 提供 qwen-max、qwen-turbo 等云端模型，以及 text-embedding-v2/v3 嵌入模型 |
| **Ollama** | 本地部署 Qwen2.5:7b 等开源模型 |
| **ChromaDB** | 本地向量数据库，用于持久化存储文档向量 |

---

## 📂 项目结构

```
Agent_Langchain_Study/
├── Langchain/
│   └── RAG基础/                          # 🎯 RAG 检索增强生成专项教程（第 19-26 课）
│       ├── 19CSVLoader.py                # CSV 文档加载器
│       ├── 20JSONLoader.py               # JSON 文档加载器
│       ├── 21TextLoader和文档分割器.py    # 文本加载 + 递归字符分割
│       ├── 22PyPDFLoder.py               # PDF 文档加载器
│       ├── 23VectorStores向量存储.py     # InMemoryVectorStore 内存向量存储
│       ├── 24外部向量持久化存储.py        # ChromaDB 持久化向量数据库
│       ├── 25基于向量检索构建提示词.py    # RAG 基础：检索 + 提示词构建
│       ├── 26RunnnablePassthrough.py      # RAG 完整实现：RunnablePassthrough 链路
│       └── dashscope_embedding_compat.py # DashScope 嵌入模型兼容层
│
├── HelloAgent/                            # Agent 应用示例
│   └── 02自定义联网搜索工具.py            # SerpApi 联网搜索工具
│
├── 01-17 (基础课程)                       # LangChain 核心概念入门
├── qwen_api_key.py                        # API Key 管理工具
└── api_key.txt                            # API Key 配置（不提交）
```

### RAG 基础项目目录说明

`Langchain/RAG基础/` 目录包含 **8 个核心文件**，系统性地讲解如何从零构建 RAG（Retrieval-Augmented Generation）检索增强生成系统：

| 编号 | 文件 | 核心功能 | 关键技术 |
|------|------|---------|---------|
| 19 | `19CSVLoader.py` | 加载结构化数据 | CSVLoader、批量加载、懒加载 |
| 20 | `20JSONLoader.py` | 解析 JSON 数据源 | JSONLoader、字段映射 |
| 21 | `21TextLoader和文档分割器.py` | 非结构化文本处理 | TextLoader + RecursiveCharacterTextSplitter |
| 22 | `22PyPDFLoder.py` | PDF 文档解析 | PyPDFLoader、页面提取 |
| 23 | `23VectorStores向量存储.py` | 内存向量存储 | InMemoryVectorStore、增删查 |
| 24 | `24外部向量持久化存储.py` | 持久化向量数据库 | ChromaDB、磁盘存储 |
| 25 | `25基于向量检索构建提示词.py` | RAG 核心流程 | similarity_search + PromptTemplate |
| 26 | `26RunnnablePassthrough.py` | 完整 RAG 链路 | RunnablePassthrough + Retriever |

---

## 🚀 快速开始

### 环境要求

- **操作系统**: Windows / macOS / Linux
- **Python 版本**: 3.8 或更高版本
- **内存要求**: 
  - 仅使用云端模型: ≥ 4GB RAM
  - 运行本地 Ollama 模型: ≥ 8GB RAM（推荐 16GB）

### 安装步骤

#### 1️⃣ 克隆项目

```bash
git clone https://github.com/CGmoke/Agent_Langchain_Study.git
cd Agent_Langchain_Study
```

#### 2️⃣ 创建虚拟环境（推荐）

```bash
# 创建虚拟环境
python -m venv .venv

# 激活虚拟环境
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

#### 3️⃣ 安装依赖

```bash
# 安装核心依赖
pip install langchain-core
pip install langchain-community
pip install langchain-openai
pip install langchain-ollama
pip install ollama

# 安装通义千问支持（包含嵌入模型）
pip install dashscope

# 安装 RAG 相关依赖（文档加载器、向量存储、文本分割器）
pip install langchain-chroma          # ChromaDB 向量数据库
pip install langchain-text-splitters  # 文本分割器
pip install chromadb                  # ChromaDB 核心库
pip install pypdf                     # PDF 解析库（可选）

# 验证安装
python -c "import langchain; print(f'LangChain 版本: {langchain.__version__}')"
```

#### 4️⃣ 配置 API Key

**方式一：创建配置文件**
```bash
# 在项目根目录创建 api_key.txt 文件
# 将你的通义千问 API Key 写入该文件（仅一行，无空格）
echo "your-api-key-here" > api_key.txt
```

**获取 API Key**: 访问 [阿里云百炼平台](https://bailian.console.aliyun.com/) 注册并获取 API Key

#### 5️⃣ （可选）安装本地模型

```bash
# 安装 Ollama（如果尚未安装）
# 访问 https://ollama.ai 下载对应操作系统的版本

# 拉取 Qwen2.5 模型（约 4.7GB）
ollama pull qwen2.5:7b

# 启动 Ollama 服务
ollama serve
```

---

## 📚 使用指南

### 学习路径建议

#### 🌱 **入门阶段**（第 1-5 课）

掌握基础的模型调用和对话交互：

```bash
# 第 1 课：OpenAI 兼容接口调用
python 01Openai库的基本使用.py

# 第 2 课：通义千问原生 SDK
python 02qwen.py

# 第 3 课：Ollama 本地模型
python 03Langchain使用ollama.py

# 第 4 课：流式输出体验
python 04langchain流式输出.py

# 第 5 课：聊天模型多轮对话
python 05Langchain调用聊天模型.py
```

#### 🌿 **进阶阶段**（第 6-12 课）

深入理解提示词系统和消息管理：

```bash
# 第 6 课：离线场景优化
python 06langchain调用ollama离线大模型.py

# 第 7 课：消息简写形式
python 07langchain消息的简写形式.py

# 第 8 课：文本嵌入模型
python 08langchain嵌入模型的使用.py

# 第 9 课：通用提示词模板
python 09langchain通用提示词.py

# 第 10 课：少样本提示词
python 10FewShot提示词模板.py

# 第 11 课：模板方法详解
python 11模板类format和invoke方法.py

# 第 12 课：对话提示词模板
python 12ChatPromptTemplate的使用.py
```

#### 🌳 **高级阶段**（第 13-17 课）

掌握链式编排、输出解析和状态管理：

```bash
# 第 13 课：Chain 链式编程
python 13chain的基础使用.py

# 第 14 课：字符串输出解析
python 14StrOutPutParser解析器.py

# 第 15 课：JSON 结构化输出
python 15JsonOutPutParser解析器.py

# 第 16 课：自定义可运行组件
python 16RunnableLambda的基础使用.py

# 第 17 课：会话记忆管理
python 17Memory临时会话记忆.py
```

#### 🚀 **RAG 检索增强生成**（第 19-26 课）⭐ 核心专项

从零构建完整的 RAG 系统，掌握文档处理、向量存储、智能检索全流程：

```bash
cd Langchain/RAG基础

# 第 19 课：CSV 文档加载器 - 结构化数据导入
python 19CSVLoader.py

# 第 20 课：JSON 文档加载器 - JSON 数据解析
python 20JSONLoader.py

# 第 21 课：文本加载与分割 - 长文档分块处理
python 21TextLoader和文档分割器.py

# 第 22 课：PDF 文档加载器 - PDF 文件解析
python 22PyPDFLoder.py

# 第 23 课：内存向量存储 - InMemoryVectorStore 基础操作
python 23VectorStores向量存储.py

# 第 24 课：持久化向量数据库 - ChromaDB 磁盘存储
python 24外部向量持久化存储.py

# 第 25 课：RAG 基础实现 - 检索 + 提示词构建
python 25基于向量检索构建提示词.py

# 第 26 课：完整 RAG 链路 - RunnablePassthrough 生产级实现 ⭐
python 26RunnnablePassthrough.py
```

---

### 核心功能演示

#### 🎯 示例 1：基本对话

```python
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# 初始化模型
model = ChatOpenAI(
    model="qwen-max",
    api_key="your-api-key",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 构建对话
response = model.invoke([
    SystemMessage(content="你是一个边塞诗人"),
    HumanMessage(content="写一首唐诗")
])

print(response.content)
```

#### 🔄 示例 2：流式输出

```python
from langchain_community.llms.tongyi import Tongyi

model = Tongyi(api_key="your-api-key", model="qwen-max")

# 流式逐字输出
for chunk in model.stream("你是谁？"):
    print(chunk, end="", flush=True)
```

#### ⛓️ 示例 3：链式组合

```python
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import StrOutputParser

# 构建处理链：提示词 → 模型 → 解析器
prompt = PromptTemplate.from_template("请为{topic}写一段简介")
model = ChatTongyi(api_key="your-api-key", model="qwen-max")
parser = StrOutputParser()

chain = prompt | model | parser

# 一键执行整个流程
result = chain.invoke({"topic": "人工智能"})
print(result)
```

#### 🧠 示例 4：会话记忆

```python
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

model = ChatTongyi(api_key="your-api-key", model="qwen-max")

# 创建带记忆的链
chain_with_memory = RunnableWithMessageHistory(
    model,
    lambda session_id: InMemoryChatMessageHistory(),
    input_messages_key="input",
    history_messages_key="chat_history"
)

# 多轮对话自动保存上下文
response1 = chain_with_memory.invoke(
    {"input": "我叫小明"},
    config={"configurable": {"session_id": "user-123"}}
)

response2 = chain_with_memory.invoke(
    {"input": "我叫什么名字？"},
    config={"configurable": {"session_id": "user-123"}}
)
# 第二次提问能记住之前的对话内容
```

#### 🔍 示例 5：RAG 检索增强生成（核心）

```python
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_community.chat_models import ChatTongyi
from langchain_core.runnables import RunnablePassthrough
from langchain_core.vectorstores import InMemoryVectorStore
from dashscope_embedding_compat import DashScopeEmbeddingCompat
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document
from qwen_api_key import get_qwen_api_key

# 1️⃣ 初始化大模型
model = ChatTongyi(api_key=get_qwen_api_key(), model="qwen3-max")

# 2️⃣ 构建 RAG 提示词模板（包含上下文占位符）
prompt = ChatPromptTemplate.from_messages([
    ("system", "以我提供的已知参考资料为主，简洁和专业的回答用户问题。参考资料：{context}。"),
    ("human", "{input}")
])

# 3️⃣ 初始化向量存储（使用兼容版嵌入模型）
vector_store = InMemoryVectorStore(
    embedding=DashScopeEmbeddingCompat(model="text-embedding-v2", api_key=get_qwen_api_key())
)

# 4️⃣ 添加文档到向量库
vector_store.add_texts([
    "简介：当生命之神林星澜在神战中陨落，骸界的血月见证了他以灵骸双生之躯苏醒。",
    "吞噬灵能、篡改法则，他誓要撕开【归墟裂隙】重返故土，却发觉灵能枯竭竟是宇宙自愈的'断臂求生'...",
    "骸骨王座下，他背负神格碎片与归寂烙印，既是众生眼中的救世主，亦是熵增规则的化身。",
])

# 5️⃣ 创建检索器（返回最相似的 k 个文档）
retriever = vector_store.as_retriever(search_kwargs={"k": 4})

# 6️⃣ 定义文档格式化函数
def format_docs(docs: list[Document]) -> str:
    """将检索到的文档列表格式化为字符串"""
    if not docs:
        return ""
    return "[" + ",".join(doc.page_content for doc in docs) + "]"

# 7️⃣ 构建 RAG 完整链路
chain = (
    {"input": RunnablePassthrough(), "context": retriever | format_docs}
    | prompt      # 注入检索结果到提示词
    | model       # 大模型推理
    | StrOutputParser()  # 解析输出
)

# 8️⃣ 执行 RAG 查询
answer = chain.invoke({"input": "简介介绍了什么"})
print(answer)
# 输出：基于向量检索到的相关文档内容生成的回答...
```

#### 📄 示例 6：文档加载与分割

```python
from langchain_community.document_loaders import TextLoader, CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 加载文本文件
loader = TextLoader("data/document.txt", encoding="utf-8")
docs = loader.load()

# 使用递归字符分割器处理长文本
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,           # 每段最大字符数
    chunk_overlap=200,         # 段间重叠字符数（保持上下文连贯）
    separators=["\n\n", "\n", "。", "！", "？", ".", ",", " ", ""],
    length_function=len,
)

# 分割文档
split_docs = text_splitter.split_documents(docs)
print(f"原始文档数: {len(docs)}, 分割后: {len(split_docs)}")
```

#### 💾 示例 7：持久化向量存储（ChromaDB）

```python
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader
from qwen_api_key import get_qwen_api_key

# 创建持久化 ChromaDB 向量数据库
vector_store = Chroma(
    collection_name="my_rag_db",                    # 集合名称
    embedding_function=DashScopeEmbeddings(
        model="text-embedding-v3",
        dashscope_api_key=get_qwen_api_key()
    ),
    persist_directory="./data/chroma"               # 持久化路径
)

# 加载并添加文档
loader = CSVLoader(file_path="data/info.csv", encoding="utf-8")
documents = loader.load()

vector_store.add_documents(
    documents=documents,
    ids=[f"doc_{i}" for i in range(len(documents))]
)

# 相似度检索
results = vector_store.similarity_search(query="搜索关键词", k=5)
for doc in results:
    print(f"- {doc.page_content[:100]}...")
```

---

## 🏗️ 架构设计

### 整体架构图

```
┌─────────────────────────────────────────────────────────────┐
│                     应用层 (Application)                      │
│  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌─────────────┐ │
│  │ 对话应用   │ │ RAG 系统  │ │ Agent     │ │ 工具调用    │ │
│  └─────┬─────┘ └─────┬─────┘ └─────┬─────┘ └──────┬──────┘ │
└────────┼────────────┼────────────┼───────────────┼─────────┘
         │            │            │               │
┌────────▼────────────▼────────────▼───────────────▼─────────┐
│                   LangChain 框架层                            │
│  ┌──────────┐  ┌──────────┐  ┌─────────────────────────┐  │
│  │ Prompts  │→ │ Chains   │→ │ Output Parsers          │  │
│  ├──────────┤  ├──────────┤  ├─────────────────────────┤  │
│  │ Messages │  │ Memory   │  │ Runnable Passthrough     │  │
│  └──────────┘  └──────────┘  └─────────────────────────┘  │
│                                                              │
│  ═══════════════════════════════════════════════════════    │
│                    RAG 核心模块层                             │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────────┐  │
│  │ Document     │→ │ Text         │→ │ Vector Store     │  │
│  │ Loaders      │  │ Splitters    │  │ (InMemory/       │  │
│  │ CSV/JSON/    │  │ Recursive    │  │  ChromaDB)       │  │
│  │ Text/PDF     │  │ CharSplitter │  │                  │  │
│  └──────────────┘  └──────────────┘  └────────┬────────┘  │
│                                                    │        │
│  ┌────────────────────────────────────────────────▼────┐  │
│  │              Retriever（检索器）                       │  │
│  │  similarity_search(query, k) → top-k 相关文档         │  │
│  └─────────────────────────────────────────────────────┘  │
└────────────────────┬───────────────────────────────────────┘
                     │
┌────────────────────▼───────────────────────────────────────┐
│                      模型接入层                              │
│  ┌──────────────────┐  ┌─────────────────────────────┐    │
│  │ 通义千问 (云端)    │  │ Ollama (本地)                │    │
│  │ • qwen3-max      │  │ • qwen2.5:7b                │    │
│  │ • qwen-turbo     │  │ • deepseek-r1:8b            │    │
│  │ • text-embedding │  │                             │    │
│  │   -v2/v3         │  │                             │    │
│  └──────────────────┘  └─────────────────────────────┘    │
└────────────────────────────────────────────────────────────┘
```

### RAG 数据流示意

```
┌─────────────────────────────────────────────────────────────────────┐
│                        RAG 检索增强生成流程                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  用户问题                                                          │
│    ↓                                                               │
│  ┌─────────────────┐                                               │
│  │ RunnablePassthrough │ ← 原样传递用户输入                         │
│  └────────┬────────┘                                               │
│           │                                                         │
│           ├──→ {"input": "用户问题"}                               │
│           │                                                         │
│           │    ┌─────────────────────────────────────┐             │
│           └──→ │ Retriever (as_retriever)            │             │
│                │  1. embed_query(用户问题)            │             │
│                │  2. similarity_search(query, k=4)   │             │
│                │  3. 返回 top-k 最相似文档            │             │
│                └──────────────┬──────────────────────┘             │
│                               │                                    │
│                               ↓                                    │
│                    [Document 列表]                                 │
│                               │                                    │
│                               ↓                                    │
│                ┌──────────────────────────────┐                   │
│                │ format_docs(docs)            │                   │
│                │ → 格式化为上下文字符串        │                   │
│                └──────────────┬───────────────┘                   │
│                               │                                    │
│                               ↓                                    │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ ChatPromptTemplate                                        │    │
│  │ System: "参考资料：{context}"                              │    │
│  │ Human:  "{input}"                                         │    │
│  │                                                            │    │
│  │ → 注入检索结果 + 用户问题生成完整提示词                     │    │
│  └──────────────────────────┬───────────────────────────────┘    │
│                             │                                     │
│                             ↓                                     │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ ChatTongyi (qwen3-max)                                   │    │
│  │ → 基于上下文进行推理生成                                  │    │
│  └──────────────────────────┬───────────────────────────────┘    │
│                             │                                     │
│                             ↓                                     │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ StrOutputParser                                         │    │
│  │ → 提取纯文本回答                                          │    │
│  └──────────────────────────┬───────────────────────────────┘    │
│                             │                                     │
│                             ↓                                     │
│                    🎯 最终答案输出                                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 传统 Chain vs RAG Chain 对比

```
传统 Chain 流程：
  用户输入 → Prompt Template → LLM 推理 → 输出解析 → 回答

RAG Chain 流程：
  用户输入 → 向量检索 → 获取相关文档 → 注入 Prompt → LLM 推理 → 基于事实的回答

核心差异：RAG 在推理前先从知识库中检索相关信息，使回答更具准确性和可追溯性。
```

---

## 📊 课程知识图谱

### 模块一：模型接入（Module 1 - Model Integration）

| 编号 | 文件 | 核心知识点 | 难度 |
|------|------|-----------|------|
| 01 | `01Openai库的基本使用.py` | OpenAI 兼容协议、环境变量配置 | ⭐ |
| 02 | `02qwen.py` | 通义千问 SDK、直接调用方式 | ⭐ |
| 03 | `03Langchain使用ollama.py` | Ollama 集成、本地模型管理 | ⭐⭐ |
| 06 | `06langchain调用ollama离线大模型.py` | 离线场景、错误处理 | ⭐⭐ |

### 模块二：对话交互（Module 2 - Conversational AI）

| 编号 | 文件 | 核心知识点 | 难度 |
|------|------|-----------|------|
| 04 | `04langchain流式输出.py` | Stream 协议、实时响应 | ⭐⭐ |
| 05 | `05Langchain调用聊天模型.py` | 多轮对话、消息类型 | ⭐⭐ |
| 07 | `07langchain消息的简写形式.py` | 元组语法、变量注入 | ⭐⭐ |
| 17 | `17Memory临时会话记忆.py` | InMemoryHistory、上下文保持 | ⭐⭐⭐ |

### 模块三：提示词工程（Module 3 - Prompt Engineering）

| 编号 | 文件 | 核心知识点 | 难度 |
|------|------|-----------|------|
| 09 | `09langchain通用提示词.py` | PromptTemplate、变量替换 | ⭐⭐ |
| 10 | `10FewShot提示词模板.py` | FewShot、少样本学习 | ⭐⭐⭐ |
| 11 | `11模板类format和invoke方法.py` | 方法对比、类型转换 | ⭐⭐ |
| 12 | `12ChatPromptTemplate的使用.py` | MessagesPlaceholder、角色定义 | ⭐⭐⭐ |

### 模块四：链式编排（Module 4 - Chaining & Parsing）

| 编号 | 文件 | 核心知识点 | 难度 |
|------|------|-----------|------|
| 13 | `13chain的基础使用.py` | LCEL 语法、管道符 \| | ⭐⭐⭐ |
| 14 | `14StrOutPutParser解析器.py` | StrOutputParser、文本提取 | ⭐⭐ |
| 15 | `15JsonOutPutParser解析器.py` | JsonOutputParser、结构化数据 | ⭐⭐⭐ |
| 16 | `16RunnableLambda的基础使用.py` | 自定义组件、函数封装 | ⭐⭐⭐ |

### 模块五：向量化（Module 5 - Embeddings）

| 编号 | 文件 | 核心知识点 | 难度 |
|------|------|-----------|------|
| 08 | `08langchain嵌入模型的使用.py` | DashScopeEmbeddings、向量生成 | ⭐⭐ |

### 模块六：RAG 检索增强生成（Module 6 - RAG）⭐

#### 6.1 文档加载与处理（Document Loading & Splitting）

| 编号 | 文件 | 核心知识点 | 难度 |
|------|------|-----------|------|
| 19 | `19CSVLoader.py` | CSVLoader、批量加载、懒加载、字段映射 | ⭐⭐ |
| 20 | `20JSONLoader.py` | JSONLoader、JSON 结构解析、数据提取 | ⭐⭐ |
| 21 | `21TextLoader和文档分割器.py` | TextLoader + RecursiveCharacterTextSplitter、分块策略 | ⭐⭐⭐ |
| 22 | `22PyPDFLoder.py` | PyPDFLoader、PDF 页面解析、元数据提取 | ⭐⭐⭐ |

#### 6.2 向量存储与检索（Vector Stores & Retrieval）

| 编号 | 文件 | 核心知识点 | 难度 |
|------|------|-----------|------|
| 23 | `23VectorStores向量存储.py` | InMemoryVectorStore、增删查操作、相似度搜索 | ⭐⭐⭐ |
| 24 | `24外部向量持久化存储.py` | ChromaDB、持久化存储、集合管理 | ⭐⭐⭐ |

#### 6.3 RAG 完整实现（RAG Implementation）

| 编号 | 文件 | 核心知识点 | 难度 |
|------|------|-----------|------|
| 25 | `25基于向量检索构建提示词.py` | similarity_search + PromptTemplate、上下文注入 | ⭐⭐⭐⭐ |
| 26 | `26RunnnablePassthrough.py` | RunnablePassthrough + Retriever、完整 RAG 链路 | ⭐⭐⭐⭐⭐ |

---

## 🔬 RAG 技术深度解析

### RAG 系统核心组件

#### 1️⃣ 文档加载器 (Document Loaders)

**作用**：将各种格式的原始数据转换为统一的 Document 对象

```python
from langchain_community.document_loaders import CSVLoader, TextLoader, PyPDFLoader

# 支持的数据源类型
loaders = {
    "csv": CSVLoader(file_path="data.csv"),           # 结构化表格数据
    "txt": TextLoader(file_path="doc.txt"),            # 纯文本文件
    "pdf": PyPDFLoader(file_path="report.pdf"),        # PDF 文档
    "json": JSONLoader(file_path="data.json"),         # JSON 数据
}

# 统一接口：返回 List[Document]
documents = loader.load()
# 每个 Document 包含：
#   - page_content: 文本内容
#   - metadata: 元数据（来源、页码等）
```

**关键特性**：
- **批量加载 vs 懒加载**：`load()` 一次性加载，`lazy_load()` 迭代器模式节省内存
- **编码支持**：自动处理 UTF-8/GBK 等多种编码
- **字段映射**：CSVLoader 支持 `source_column` 指定来源字段

#### 2️⃣ 文本分割器 (Text Splitters)

**作用**：将长文档切分为适合嵌入模型处理的文本块

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,        # 每个文本块的最大字符数
    chunk_overlap=200,       # 相邻块之间的重叠字符数（保持上下文连贯）
    separators=[             # 分割优先级（从高到低）
        "\n\n",              # 1. 段落分隔
        "\n",                # 2. 行分隔
        "。", "！", "？",     # 3. 中文句末标点
        ".", ",", " ", ""    # 4. 英文标点和字符
    ],
    length_function=len,     # 长度计算函数
)
```

**分割策略原理**：
1. 尝试用最高优先级分隔符分割
2. 如果块仍超过 `chunk_size`，使用下一级分隔符
3. 最终按字符强制截断
4. `chunk_overlap` 确保边界处信息不丢失

#### 3️⃣ 嵌入模型 (Embedding Models)

**作用**：将文本转换为高维向量，用于语义相似度计算

```python
# 方式一：官方 DashScopeEmbeddings（需要兼容处理）
from langchain_community.embeddings import DashScopeEmbeddings
embedding = DashScopeEmbeddings(
    model="text-embedding-v2",          # 或 v3（支持自定义维度）
    dashscope_api_key="your-api-key"
)

# 方式二：兼容版 DashScopeEmbeddingCompat（推荐 ✅）
from dashscope_embedding_compat import DashScopeEmbeddingCompat
embedding = DashScopeEmbeddingCompat(
    model="text-embedding-v2",
    api_key=get_qwen_api_key()           # 自动处理 SDK 兼容性问题
)

# 使用示例
vectors = embedding.embed_documents(["文本1", "文本2"])
query_vector = embedding.embed_query("查询文本")
print(f"向量维度: {len(query_vector)}")  # v2: 1536维, v3: 可配置
```

**模型对比**：

| 模型 | 维度 | 特点 | 适用场景 |
|------|------|------|---------|
| text-embedding-v1 | 1536 | 基础版本 | 简单场景 |
| text-embedding-v2 | 1536 | 中文优化 | 通用中文 RAG |
| text-embedding-v3 | 1024-4096 | 可定制维度 | 高精度需求 |

#### 4️⃣ 向量存储 (Vector Stores)

**InMemoryVectorStore - 内存存储**（适合开发测试）

```python
from langchain_core.vectorstores import InMemoryVectorStore

vector_store = InMemoryVectorStore(embedding=embedding)

# 添加文本
vector_store.add_texts(["文档1", "文档2", ...])

# 添加带 ID 的文档
vector_store.add_documents(documents, ids=["id1", "id2", ...])

# 删除文档
vector_store.delete(["id1", "id2"])

# 相似度搜索
results = vector_store.similarity_search(
    query="搜索关键词",
    k=5                           # 返回最相似的 top-k 个结果
)

# 转换为检索器（用于 Chain）
retriever = vector_store.as_retriever(
    search_kwargs={"k": 4}       # 检索参数
)
```

**ChromaDB - 持久化存储**（适合生产环境）

```python
from langchain_chroma import Chroma

# 创建持久化数据库
vector_store = Chroma(
    collection_name="my_rag_db",
    embedding_function=embedding,
    persist_directory="./data/chroma"    # 数据保存到磁盘
)

# 数据会自动持久化，重启后仍可检索
results = vector_store.similarity_search("查询", k=10)
```

**选择建议**：
- 开发/测试 → InMemoryVectorStore（简单快速）
- 生产环境 → ChromaDB（支持大规模数据、持久化、过滤查询）

#### 5️⃣ RunnablePassthrough - RAG 链路编排

**核心作用**：在 Chain 中原样传递输入数据，同时并行执行检索

```python
from langchain_core.runnables import RunnablePassthrough

chain = (
    {
        "input": RunnablePassthrough(),      # ← 用户问题原样传递
        "context": retriever | format_docs   # ← 并行执行检索和格式化
    }
    | prompt                                 # 组装提示词
    | model                                  # LLM 推理
    | StrOutputParser()                      # 提取回答
)
```

**工作原理**：
1. `RunnablePassthrough()` 将用户输入直接映射到 `"input"` 键
2. `retriever | format_docs` 构成子链：先检索再格式化
3. 两者并行执行，结果合并为字典 `{"input": ..., "context": ...}`
4. 字典传入 PromptTemplate，生成最终提示词

---

## 🤝 贡献指南

我们非常欢迎社区贡献！无论是修复 Bug、添加新示例还是改进文档。

### 分支策略

```
master (主分支)
  └── feature/xxx (功能分支开发)
       └── develop (测试分支)
            └── hotfix/xxx (紧急修复)
```

### 开发流程

#### 1️⃣ Fork 并克隆

```bash
# Fork 本仓库到你的 GitHub 账户
# 然后克隆到本地
git clone https://github.com/YOUR_USERNAME/Agent_Langchain_Study.git
cd Agent_Langchain_Study

# 添加上游仓库
git remote add upstream https://github.com/CGmoke/Agent_Langchain_Study.git
```

#### 2️⃣ 创建功能分支

```bash
# 从 master 创建新分支
git checkout -b feature/your-feature-name
```

#### 3️⃣ 开发并测试

```bash
# 编写代码并确保所有示例可运行
python your_new_example.py

# 添加必要的注释和文档
```

#### 4️⃣ 提交代码

遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

```bash
git add .
git commit -m "feat: 添加 RAG 检索增强生成示例"

# 提交信息格式：
# type(scope): subject
#
# type 类型：
#   feat:     新功能
#   fix:      修复 Bug
#   docs:     文档更新
#   style:    代码格式调整
#   refactor: 重构代码
#   test:     测试相关
#   chore:    构建/工具变更
```

#### 5️⃣ 推送并创建 PR

```bash
# 推送到你的 fork
git push origin feature/your-feature-name

# 在 GitHub 上创建 Pull Request
# 填写清晰的 PR 描述：
# - 变更目的
# - 测试结果
# - 相关 Issue（如有）
```

#### PR 检查清单

- [ ] 代码符合 PEP 8 规范
- [ ] 所有示例可以独立运行
- [ ] 包含充分的中文注释
- [ ] 更新相关文档（README 或课程索引）
- [ ] 通过本地测试验证

---

## 📝 代码规范

### Python 代码风格

```python
# ✅ 正确示例：清晰的中文注释 + 合理的命名
def get_qwen_api_key():
    """获取通义千问 API Key"""
    if "QWEN_API_KEY" not in os.environ:
        with open("api_key.txt", "r") as f:
            os.environ["QWEN_API_KEY"] = f.read().strip()
    return os.environ["QWEN_API_KEY"]

# ❌ 避免：无注释或英文注释
def get_key():
    f = open('key.txt')
    return f.read()
```

### 文件命名规范

- 使用数字前缀标识课程顺序：`01_xxx.py`, `02_xxx.py`
- 文件名使用下划线分隔：`chat_prompt_template_demo.py`
- 避免使用中文文件名

### 注释要求

每个示例文件必须包含：

1. **文件头注释**：说明本课的核心知识点
2. **关键行内注释**：解释重要逻辑
3. **函数文档字符串**：描述参数和返回值

---

## ❓ 常见问题（FAQ）

### 基础问题

#### Q1: 如何获取通义千问 API Key？

**A**: 
1. 访问 [阿里云百炼平台](https://bailian.console.aliyun.com/)
2. 注册/登录阿里云账号
3. 进入「API-KEY 管理」页面
4. 创建新的 API Key 并复制

#### Q2: Ollama 启动失败怎么办？

**A**: 
```bash
# 检查 Ollama 是否正确安装
ollama --version

# 手动启动服务
ollama serve

# 查看已安装的模型
ollama list

# 如果端口被占用，检查 11434 端口
netstat -ano | findstr :11434
```

#### Q3: 出现 502 错误如何解决？

**A**: 这是 `langchain-ollama` 库的已知兼容性问题。解决方案：

1. **升级库版本**：
   ```bash
   pip install --upgrade langchain-ollama ollama
   ```

2. **直接调用 Ollama API**（绕过问题库）：
   ```python
   import requests
   
   response = requests.post(
       'http://localhost:11434/api/chat',
       json={'model': 'qwen2.5:7b', 'messages': [...], 'stream': True},
       stream=True
   )
   ```

3. **使用更稳定的模型**：尝试 `deepseek-r1:8b` 等其他模型

#### Q4: 内存不足怎么处理？

**A**: 
- 减小模型规模：使用 `qwen2.5:3b`（约 2GB）代替 `qwen2.5:7b`
- 关闭其他占用内存的程序
- 增加 swap 空间（Linux）或虚拟内存（Windows）

#### Q5: 如何切换使用不同的模型？

**A**: 
```python
# 云端模型（需要 API Key）
model = ChatOpenAI(model="qwen-max", ...)  # 最强性能
model = ChatOpenAI(model="qwen-turbo", ...)  # 更快响应

# 本地模型（需要 Ollama）
model = ChatOllama(model="qwen2.5:7b")  # 通用场景
model = ChatOllama(model="deepseek-r1:8b")  # 推理能力更强
```

---

### RAG 专项问题 ⭐

#### Q6: DashScope 嵌入模型报错 `input.texts should be array` 怎么解决？

**A**: 这是 `langchain-community` 与新版 DashScope SDK (v1.25+) 的兼容性问题。

**解决方案**：使用项目提供的兼容层 `DashScopeEmbeddingCompat`

```python
# ❌ 错误方式（会报错）
from langchain_community.embeddings import DashScopeEmbeddings
embedding = DashScopeEmbeddings(model="text-embedding-v2", ...)

# ✅ 正确方式（使用兼容层）
from dashscope_embedding_compat import DashScopeEmbeddingCompat
embedding = DashScopeEmbeddingCompat(
    model="text-embedding-v2",
    api_key=get_qwen_api_key()  # 自动处理所有兼容性问题
)
```

**兼容层特性**：
- 自动处理 LangChain 多线程环境下的参数类型转换
- 支持 text-embedding-v1/v2/v3 所有版本
- 包含完善的错误处理和重试机制

#### Q7: 文档分割时 `chunk_size` 和 `chunk_overlap` 如何设置？

**A**: 参数选择取决于文档类型和嵌入模型：

| 场景 | chunk_size | chunk_overlap | 说明 |
|------|-----------|---------------|------|
| 短文章/FAQ | 500 | 50 | 信息密度高，小块即可 |
| 技术文档 | 1000 | 200 | 平衡上下文和精度 |
| 长篇小说 | 2000 | 400 | 保持叙事连贯性 |
| 法律合同 | 1500 | 300 | 条款完整性重要 |

**调优建议**：
- `chunk_size` 不超过嵌入模型的上下文窗口（通常 512-8192 tokens）
- `chunk_overlap` 一般设为 `chunk_size` 的 10%-20%
- 中文文档建议使用中文标点作为分隔符

#### Q8: InMemoryVectorStore vs ChromaDB 如何选择？

**A**: 

| 特性 | InMemoryVectorStore | ChromaDB |
|------|---------------------|----------|
| **持久化** | ❌ 程序结束数据丢失 | ✅ 数据保存到磁盘 |
| **性能** | ⚡⚡⚡ 极快（内存操作） | ⚡⚡ 快（需磁盘 I/O） |
| **数据规模** | < 10万文档 | 百万级+ 文档 |
| **适用场景** | 开发测试、演示 | 生产环境、长期使用 |
| **部署复杂度** | 简单（无需额外服务） | 中等（需管理数据库文件） |

**推荐策略**：
```python
# 开发阶段
vector_store = InMemoryVectorStore(embedding=embedding)

# 上线前迁移到 ChromaDB
from langchain_chroma import Chroma
vector_store = Chroma(
    collection_name="production_db",
    embedding_function=embedding,
    persist_directory="./data/chroma"
)
```

#### Q9: RAG 检索结果不准确怎么办？

**A**: 检索质量优化策略：

**1️⃣ 优化文档预处理**
```python
# 清洗文本，去除噪声
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)        # 合并多余空白
    text = re.sub(r'[^\w\s\u4e00-\u9fff]', '', text)  # 保留中英文
    return text.strip()
```

**2️⃣ 调整检索参数**
```python
retriever = vector_store.as_retriever(
    search_type="similarity_score_threshold",  # 使用阈值过滤
    search_kwargs={
        "k": 6,                    # 增加返回数量
        "score_threshold": 0.7     # 只保留相似度 > 0.7 的结果
    }
)
```

**3️⃣ 改进提示词模板**
```python
prompt = ChatPromptTemplate.from_messages([
    ("system", """你是一个专业的问答助手。
请严格基于以下参考资料回答问题。
如果资料中没有相关信息，请明确说明'无法从给定资料中找到答案'。

参考资料：
{context}"""),
    ("human", "{input}")
])
```

**4️⃣ 使用混合检索（高级）**
```python
# 结合关键词检索 + 语义检索
retriever = vector_store.as_retriever(
    search_type="mmr",  # Maximal Marginal Relevance
    search_kwargs={"k": 5, "fetch_k": 20}
)
```

#### Q10: 如何评估 RAG 系统的效果？

**A**: 常用评估指标：

**检索质量指标**：
- **Precision@K**：Top-K 结果中相关文档的比例
- **Recall@K**：所有相关文档中被检索到的比例
- **MRR (Mean Reciprocal Rank)**：第一个相关结果的平均排名

**生成质量指标**：
- **忠实度 (Faithfulness)**：回答是否基于检索到的文档（非幻觉）
- **相关性 (Relevance)**：回答是否解决了用户的问题
- **上下文精确度**：回答中引用的信息是否准确

**快速自测方法**：
```python
test_questions = [
    {"question": "问题1", "expected_keywords": ["关键词1", "关键词2"]},
    {"question": "问题2", "expected_keywords": ["关键词3"]},
]

for test in test_questions:
    answer = chain.invoke({"input": test["question"]})
    # 检查回答是否包含预期关键词
    hits = sum(1 for kw in test["expected_keywords"] if kw in answer)
    print(f"Q: {test['question']}\nA: {answer[:100]}...\nHits: {hits}/{len(test['expected_keywords'])}\n")
```

---

## 📈 学习路线图

```
Week 1-2: 基础入门
├── 理解 LangChain 核心概念
├── 掌握模型调用方式（云端 + 本地）
└── 实践流式输出和多轮对话

Week 3-4: 提示词进阶
├── 深入学习三大模板体系
├── 掌握少样本学习技巧
└── 设计复杂对话场景

Week 5-6: 链式编排
├── 理解 LCEL 编程范式
├── 构建多步骤处理流水线
└── 实现结构化输出解析

Week 7-8: RAG 检索增强生成 ⭐ 核心专项
├── 文档加载：CSV/JSON/Text/PDF 多格式支持
├── 文本分割：RecursiveCharacterTextSplitter 分块策略
├── 向量化：DashScope 嵌入模型与兼容层使用
├── 向量存储：InMemoryVectorStore vs ChromaDB 选型
├── 相似度检索：similarity_search 与 Retriever 模式
├── RAG 链路：RunnablePassthrough 完整实现
└── 生产优化：持久化存储、性能调优、效果评估

Week 9+: 高级应用
├── 集成外部工具和 API
├── 开发完整的 Agent 应用
├── 实现 Multi-RAG（多数据源融合）
└── 部署上线与监控
```

### RAG 学习路径详解

```
第 19-20 课：文档加载基础 (2 天)
├── 目标：掌握从不同数据源加载文档的能力
├── 练习：
│   ├── 准备 CSV/JSON/TXT/PDF 测试文件
│   ├── 实现批量加载和懒加载对比
│   └── 提取文档元数据并分析结构
└── 产出：可复用的文档加载工具函数

第 21-22 课：文本分割策略 (2 天)
├── 目标：理解如何将长文档切分为合适的文本块
├── 练习：
│   ├── 调整 chunk_size 和 chunk_overlap 观察效果
│   ├── 对比不同 separators 的分割结果
│   └── 处理特殊格式（代码、表格、列表）
└── 产出：针对特定文档类型的最佳分割配置

第 23-24 课：向量存储实践 (3 天)
├── 目标：掌握向量数据库的 CRUD 操作
├── 练习：
│   ├── InMemoryVectorStore 基础操作（增删查）
│   ├── ChromaDB 持久化存储与恢复
│   └── 性能测试：不同数据规模下的查询速度
└── 产出：生产就绪的向量存储管理模块

第 25-26 课：RAG 完整实现 (3 天) ⭐
├── 目标：构建端到端的 RAG 应用系统
├── 练习：
│   ├── 手动实现 RAG 流程（理解原理）
│   ├── 使用 RunnablePassthrough 重构（生产级）
│   ├── 对比不同 k 值对回答质量的影响
│   └── 添加错误处理和日志记录
└── 产出：可直接部署的 RAG 问答系统
```

---

## 🙏 致谢

- **LangChain 团队** - 提供强大的 AI 应用开发框架
- **阿里云** - 提供通义千问大模型服务和 DashScope 嵌入模型
- **Ollama** - 让本地运行大模型变得简单
- **Qwen 团队** - 开源优秀的中文大模型（Qwen2.5/Qwen3）
- **ChromaDB 团队** - 提供轻量级向量数据库解决方案
- **黑马程序员** - 提供免费的教学视频和 LangChain 学习路径

---

## 📄 许可证

本项目采用 [MIT License](LICENSE) 开源协议。

```
MIT License

Copyright (c) 2024 CGmoke

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 📮 联系方式

- **作者**: CGmoke
- **邮箱**: 3059342114@qq.com
- **GitHub**: [https://github.com/CGmoke](https://github.com/CGmoke)
- **项目地址**: [https://github.com/CGmoke/Agent_Langchain_Study](https://github.com/CGmoke/Agent_Langchain_Study)

---

## ⭐ Star 支持

如果这个项目对你有帮助，欢迎给一个 ⭐ Star 支持一下！你的支持是我持续更新的动力 💪


**让 AI 开发变得更简单、更有趣！**

Made with ❤️ by CGmoke

