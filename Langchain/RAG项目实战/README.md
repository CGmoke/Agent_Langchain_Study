# 🛒 线上服装购买智能客服系统

> **基于 LangChain + Streamlit 构建的生产级 RAG 检索增强生成应用**

---

## 📖 项目概述

本项目是一个**完整的 RAG（Retrieval-Augmented Generation）智能客服系统**，专为线上服装购买场景设计。系统集成了文档知识库管理、向量检索、大模型推理、会话记忆等核心功能，提供了开箱即用的 Web 界面。

### 🎯 应用场景

- **电商客服**：自动回答尺码推荐、洗涤养护、颜色选择等问题
- **知识库问答**：基于企业文档构建智能问答系统
- **多轮对话**：支持上下文记忆的连续对话体验

### ✨ 核心特性

| 特性 | 说明 |
|------|------|
| 🔍 **RAG 检索增强** | 基于向量检索的知识库问答，回答准确可靠 |
| 💬 **多轮对话** | 支持会话历史记忆，上下文连贯 |
| 📚 **知识库管理** | Web 界面上传文档，自动分割、向量化、存储 |
| 💾 **持久化存储** | ChromaDB 向量数据库 + 文件历史记录 |
| 🌐 **Web 界面** | Streamlit 构建的友好交互界面 |
| ⚡ **流式输出** | 实时显示 AI 回复，提升用户体验 |

---

## 🏗️ 系统架构

```
┌─────────────────────────────────────────────────────────────────────┐
│                        用户交互层 (Streamlit)                         │
│  ┌─────────────────────────┐  ┌─────────────────────────────────┐  │
│  │   app_qa.py             │  │   app_file_uploader.py          │  │
│  │   智能客服问答界面        │  │   知识库文档上传界面             │  │
│  └───────────┬─────────────┘  └───────────────┬─────────────────┘  │
└──────────────┼────────────────────────────────┼────────────────────┘
               │                                │
┌──────────────▼────────────────────────────────▼────────────────────┐
│                        业务逻辑层                                     │
│  ┌─────────────────────────┐  ┌─────────────────────────────────┐  │
│  │   RagService            │  │   KnowledgeBaseService          │  │
│  │   - RAG 链路编排         │  │   - 文档上传处理                 │  │
│  │   - 会话历史管理         │  │   - 文本分割                     │  │
│  │   - 提示词模板           │  │   - MD5 去重                     │  │
│  └───────────┬─────────────┘  └───────────────┬─────────────────┘  │
└──────────────┼────────────────────────────────┼────────────────────┘
               │                                │
┌──────────────▼────────────────────────────────▼────────────────────┐
│                        数据存储层                                     │
│  ┌─────────────────────────┐  ┌─────────────────────────────────┐  │
│  │   VectorStoreService    │  │   FileChatMessageHistory        │  │
│  │   - ChromaDB 向量存储    │  │   - JSON 文件会话历史            │  │
│  │   - 相似度检索           │  │   - 多用户会话隔离               │  │
│  └───────────┬─────────────┘  └───────────────┬─────────────────┘  │
│              │                                │                    │
│  ┌───────────▼─────────────┐  ┌───────────────▼─────────────────┐  │
│  │   ./chroma_db/          │  │   ./chat_history/               │  │
│  │   向量数据库文件          │  │   会话历史文件                   │  │
│  └─────────────────────────┘  └─────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
               │
┌──────────────▼────────────────────────────────────────────────────┐
│                        模型服务层                                    │
│  ┌─────────────────────────┐  ┌─────────────────────────────────┐  │
│  │   ChatTongyi (qwen3-max)│  │   DashScopeEmbeddings           │  │
│  │   通义千问对话模型        │  │   text-embedding-v3 嵌入模型     │  │
│  └─────────────────────────┘  └─────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 📂 项目结构

```
RAG项目实战/
├── 📄 核心模块
│   ├── Rag.py                    # RAG 服务核心类（链路编排、检索、生成）
│   ├── vector_stores.py          # 向量存储服务（ChromaDB 封装）
│   ├── knowledge_base.py         # 知识库管理服务（上传、分割、向量化）
│   ├── file_history_store.py     # 文件会话历史管理
│   └── config_data.py            # 全局配置文件
│
├── 🌐 Web 应用
│   ├── app_qa.py                 # 智能客服问答界面
│   └── app_file_uploader.py      # 知识库文档上传界面
│
├── 📁 数据目录
│   ├── data/                     # 示例知识库文档
│   │   ├── 尺码推荐.txt
│   │   ├── 洗涤养护.txt
│   │   └── 颜色选择.txt
│   ├── chroma_db/                # ChromaDB 向量数据库（自动生成）
│   ├── chat_history/             # 会话历史记录（自动生成）
│   └── md5.txt                   # 文档 MD5 去重记录
│
├── 🔑 配置文件
│   ├── api_key.txt               # 通义千问 API Key（需自行配置）
│   └── qwen_api_key.py           # API Key 加载工具
│
└── README.md                     # 项目说明文档
```

---

## 🚀 快速开始

### 环境要求

| 依赖 | 版本 | 说明 |
|------|------|------|
| Python | 3.8+ | 编程语言 |
| langchain-core | Latest | LangChain 核心框架 |
| langchain-community | Latest | 社区集成组件 |
| langchain-chroma | Latest | ChromaDB 向量数据库 |
| langchain-text-splitters | Latest | 文本分割器 |
| streamlit | Latest | Web 界面框架 |
| dashscope | Latest | 通义千问 SDK |

### 安装步骤

#### 1️⃣ 克隆项目

```bash
git clone https://github.com/CGmoke/Agent_Langchain_Study.git
cd Agent_Langchain_Study/Langchain/RAG项目实战
```

#### 2️⃣ 创建虚拟环境（推荐）

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

#### 3️⃣ 安装依赖

```bash
pip install langchain-core
pip install langchain-community
pip install langchain-chroma
pip install langchain-text-splitters
pip install streamlit
pip install dashscope
pip install chromadb
```

#### 4️⃣ 配置 API Key

在 `RAG项目实战` 目录下创建 `api_key.txt` 文件：

```bash
# 将你的通义千问 API Key 写入文件
echo "your-dashscope-api-key" > api_key.txt
```

**获取 API Key**：访问 [阿里云百炼平台](https://bailian.console.aliyun.com/) 注册并获取

---

## 📚 使用指南

### 启动智能客服问答系统

```bash
streamlit run app_qa.py
```

**功能说明**：
- 输入服装相关问题（如"夏天穿什么颜色衣服"）
- 系统自动检索知识库并生成回答
- 支持多轮对话，自动记忆上下文
- 流式输出，实时显示回复

### 启动知识库管理界面

```bash
streamlit run app_file_uploader.py
```

**功能说明**：
- 上传 TXT 文档到知识库
- 自动进行文本分割、向量化、存储
- 支持 MD5 去重，避免重复上传

### 命令行测试

```bash
# 测试 RAG 服务
python rag.py

# 测试向量检索
python vector_stores.py

# 测试知识库上传
python knowledge_base.py
```

---

## ⚙️ 配置说明

### 核心配置项 (`config_data.py`)

```python
# ChromaDB 向量数据库配置
collection_name = "rag"              # 集合名称
persist_directory = "./chroma_db"    # 持久化路径

# 文本分割器配置
chunk_size = 500                     # 文本块最大长度
chunk_overlap = 50                   # 块间重叠字符数
separators = ["\n\n", "\n", "。", "！", "？", ...]  # 分隔符
max_split_char_size = 1000           # 触发分割的阈值

# 检索配置
similarity_threshold = 1             # 返回的文档数量

# 模型配置
embedding_model = "text-embedding-v3"  # 嵌入模型
chat_model = "qwen3-max"              # 对话模型

# 会话配置
session_config = {
    "configurable": {
        "session_id": "user_001",    # 会话 ID（支持多用户）
    }
}
```

### 参数调优建议

| 参数 | 默认值 | 调优建议 |
|------|--------|---------|
| `chunk_size` | 500 | 技术文档建议 1000，FAQ 建议 300 |
| `chunk_overlap` | 50 | 一般设为 chunk_size 的 10% |
| `similarity_threshold` | 1 | 增大可提高召回率，但可能降低精度 |

---

## 🔧 核心模块详解

### 1️⃣ RagService - RAG 服务核心

**功能**：编排完整的 RAG 链路

```python
from Rag import RagService

# 初始化服务
rag = RagService()

# 执行问答
response = rag.chain.invoke(
    {"input": "夏天穿什么颜色衣服"},
    session_config
)

# 流式输出
for chunk in rag.chain.stream({"input": "问题"}, session_config):
    print(chunk, end="")
```

**核心流程**：
1. 用户输入 → RunnablePassthrough 传递
2. 检索器 → 向量相似度搜索
3. 文档格式化 → 构建上下文
4. 提示词模板 → 注入上下文和历史
5. 大模型推理 → 生成回答
6. 会话历史 → 自动保存对话

### 2️⃣ KnowledgeBaseService - 知识库管理

**功能**：文档上传、分割、向量化、存储

```python
from knowledge_base import KnowledgeBaseService

service = KnowledgeBaseService()

# 上传文本
result = service.upload_by_str(
    data="文档内容...",
    filename="文档名称.txt"
)
# 返回: "上传成功" 或 "文件已处理"
```

**特性**：
- **MD5 去重**：自动检测重复文档
- **智能分割**：长文档自动分块
- **元数据管理**：记录来源和创建时间

### 3️⃣ VectorStoreService - 向量存储

**功能**：ChromaDB 向量数据库封装

```python
from vector_stores import VectorStoreService
from langchain_community.embeddings import DashScopeEmbeddings

embedding = DashScopeEmbeddings(model="text-embedding-v3", ...)
service = VectorStoreService(embedding)

# 获取检索器
retriever = service.get_retriever()

# 执行检索
docs = retriever.invoke("查询文本")
```

### 4️⃣ FileChatMessageHistory - 会话历史

**功能**：基于文件的会话历史持久化

```python
from file_history_store import get_history

# 获取指定用户的会话历史
history = get_history("user_001")

# 自动保存对话
# 存储路径: ./chat_history/user_001
```

---

## 📊 RAG 数据流

```
用户问题: "夏天穿什么颜色衣服"
    │
    ▼
┌─────────────────────────────────────────────────────────┐
│ RunnablePassthrough                                      │
│ → 原样传递用户输入                                        │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│ Retriever (as_retriever)                                │
│ 1. embed_query("夏天穿什么颜色衣服")                      │
│ 2. similarity_search(query, k=1)                        │
│ 3. 返回最相关的文档片段                                   │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│ format_document(docs)                                   │
│ → 格式化为: "文档片段: xxx\n文档元数据: xxx"               │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│ ChatPromptTemplate                                      │
│ System: "参考资料：{context}"                            │
│ System: "用户对话历史记录如下："                          │
│ [chat_history]                                          │
│ User: "请回答用户问题：{input}"                           │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│ ChatTongyi (qwen3-max)                                  │
│ → 基于上下文和历史进行推理                                │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│ StrOutputParser                                         │
│ → 提取纯文本回答                                         │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
              🎯 最终答案输出
```

---

## ⚠️ 注意事项

### API Key 安全

- ✅ **正确做法**：将 `api_key.txt` 添加到 `.gitignore`
- ❌ **错误做法**：将 API Key 硬编码到代码中

### 数据持久化

- `chroma_db/` 目录包含向量数据库，删除后需重新导入知识库
- `chat_history/` 目录包含会话历史，删除后对话记录将丢失
- `md5.txt` 记录已处理文档，删除后可能导致重复上传

### 性能优化

1. **批量导入**：大量文档建议分批上传
2. **向量维度**：text-embedding-v3 支持自定义维度，可降低存储成本
3. **检索数量**：`similarity_threshold` 增大会增加响应时间

### 常见问题

#### Q1: 启动报错 `ModuleNotFoundError`

**A**: 确保在 `RAG项目实战` 目录下运行，且已安装所有依赖

```bash
cd Langchain/RAG项目实战
pip install -r requirements.txt  # 如果有 requirements.txt
```

#### Q2: 检索结果为空

**A**: 检查知识库是否有数据

```bash
# 查看向量数据库
ls chroma_db/

# 重新上传知识库
streamlit run app_file_uploader.py
```

#### Q3: API 调用失败

**A**: 检查 API Key 是否正确

```bash
# 查看 API Key 文件
cat api_key.txt

# 确认 API Key 有效
# 访问 https://bailian.console.aliyun.com/ 检查配额
```

---

## 🔄 扩展开发

### 添加新的知识库文档

```python
from knowledge_base import KnowledgeBaseService

service = KnowledgeBaseService()

# 方式一：上传文件内容
with open("新文档.txt", "r", encoding="utf-8") as f:
    service.upload_by_str(f.read(), "新文档.txt")

# 方式二：直接传入字符串
service.upload_by_str("这是新的知识库内容...", "自定义内容.txt")
```

### 自定义提示词模板

```python
# 在 rag.py 中修改 prompt_template
self.prompt_template = ChatPromptTemplate.from_messages([
    ("system", "你是一个专业的服装顾问。请基于以下参考资料回答：{context}"),
    ("system", "对话历史："),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
])
```

### 集成其他向量数据库

```python
# 替换 ChromaDB 为 FAISS
from langchain_community.vectorstores import FAISS

# 在 vector_stores.py 中修改
self.vector_store = FAISS.from_documents(
    documents, 
    embedding=self.embedding
)
```

---

## 📈 后续规划

- [ ] 支持更多文档格式（PDF、Word、Markdown）
- [ ] 添加混合检索（关键词 + 语义）
- [ ] 实现多用户权限管理
- [ ] 添加检索结果评分和过滤
- [ ] 支持 Agent 工具调用（联网搜索等）

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建功能分支：`git checkout -b feature/your-feature`
3. 提交更改：`git commit -m "feat: 添加新功能"`
4. 推送分支：`git push origin feature/your-feature`
5. 创建 Pull Request

---

## 📄 许可证

本项目采用 [MIT License](../../LICENSE) 开源协议。

---

## 🙏 致谢

- **LangChain** - 强大的 LLM 应用开发框架
- **阿里云通义千问** - 优秀的中文大模型服务
- **ChromaDB** - 轻量级向量数据库
- **Streamlit** - 简洁的 Web 应用框架
- **黑马程序员** - 提供免费的教学视频和 LangChain 学习路径

---

## 📮 联系方式

- **作者**: CGmoke
- **邮箱**: 3059342114@qq.com
- **GitHub**: [https://github.com/CGmoke](https://github.com/CGmoke)

---

**Made with ❤️ by CGmoke**
