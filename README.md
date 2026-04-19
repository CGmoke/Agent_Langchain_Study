# 🤖 Agent_Langchain_Study - LangChain 框架学习指南

> **从入门到精通的 LangChain 实战教程，涵盖大模型调用、提示词工程、链式编排、输出解析与记忆管理等核心技能**

---

## 📖 项目简介

本项目是一个**系统性学习 LangChain 框架的实战教程仓库**，包含 **17+ 个精心设计的示例代码**，覆盖了 LangChain 的核心概念和最佳实践。通过循序渐进的学习路径，帮助开发者快速掌握使用 LangChain 构建智能应用的关键技术。

### ✨ 核心特性

- 🔥 **多模型支持**: 同时支持云端大模型（通义千问）和本地离线模型（Ollama/Qwen2.5）
- 💬 **对话式交互**: 支持多轮对话、流式输出、消息格式化等完整对话功能
- 🎯 **提示词工程**: 深入讲解 PromptTemplate、ChatPromptTemplate、FewShotPromptTemplate 三大模板体系
- ⛓️ **链式编排**: 掌握 Chain 组合模式，构建复杂的 AI 应用流程
- 🔧 **输出解析**: 支持 JSON、字符串等多种格式的结构化输出解析
- 🧠 **会话记忆**: 实现基于内存的上下文保持和多轮对话管理
- 📚 **实战导向**: 每个示例都是可运行的独立脚本，即学即用

---

## 🛠️ 技术栈说明

### 核心依赖

| 技术 | 版本 | 用途 |
|------|------|------|
| **Python** | 3.8+ | 编程语言 |
| **langchain-core** | Latest | LangChain 核心框架 |
| **langchain-community** | Latest | 社区集成组件 |
| **langchain-openai** | Latest | OpenAI 兼容接口 |
| **langchain_ollama** | Latest | Ollama 本地模型集成 |
| **通义千问 API** | DashScope | 云端大模型服务 |
| **Ollama** | Latest | 本地大模型运行时 |

### 外部服务

| 服务 | 说明 |
|------|------|
| **阿里云通义千问** | 提供 qwen-max、qwen-turbo 等云端模型 |
| **Ollama** | 本地部署 Qwen2.5:7b 等开源模型 |

---

## 📂 项目结构

```
Agent_Langchain_Study/
├── 01Openai库的基本使用.py              # 基础：OpenAI 兼容 API 调用
├── 02qwen.py                            # 通义千问原生 SDK 使用
├── 03Langchain使用ollama.py             # Ollama 本地模型集成
├── 04langchain流式输出.py               # 流式响应处理
├── 05Langchain调用聊天模型.py           # 多轮对话实现
├── 06langchain调用ollama离线大模型.py    # 离线场景优化
├── 07langchain消息的简写形式.py         # 消息格式简化语法
├── 08langchain嵌入模型的使用.py         # 文本嵌入向量生成
├── 09langchain通用提示词.py             # PromptTemplate 基础用法
├── 10FewShot提示词模板.py               # 少样本学习提示词
├── 11模板类format和invoke方法.py        # 模板方法详解
├── 12ChatPromptTemplate的使用.py        # 对话专用模板
├── 13chain的基础使用.py                 # LCEL 链式编程
├── 14StrOutPutParser解析器.py           # 字符串输出解析
├── 15JsonOutPutParser解析器.py          # JSON 结构化输出
├── 16RunnableLambda的基础使用.py        # 自定义可运行组件
├── 17Memory临时会话记忆.py              # 会话历史管理
├── qwen_api_key.py                      # API Key 管理工具
└── api_key.txt                          # API Key 配置（不提交）
```

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

# 安装通义千问支持
pip install dashscope
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

---

## 🏗️ 架构设计

### 整体架构图

```
┌─────────────────────────────────────────────────────┐
│                   应用层 (Application)                │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐   │
│  │ 对话应用 │ │ RAG 系统 │ │ Agent   │ │ 工具调用│   │
│  └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘   │
└───────┼──────────┼──────────┼──────────┼───────────┘
        │          │          │          │
┌───────▼──────────▼──────────▼──────────▼───────────┐
│                  LangChain 框架层                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────┐  │
│  │ Prompts  │→ │ Chains   │→ │ Output Parsers   │  │
│  ├──────────┤  ├──────────┤  ├──────────────────┤  │
│  │ Messages │  │ Memory   │  │ Runnable Lambda  │  │
│  └──────────┘  └──────────┘  └──────────────────┘  │
└───────┬──────────┬──────────┬───────────────────────┘
        │          │          │
┌───────▼──────────▼──────────▼───────────────────────┐
│                    模型接入层                         │
│  ┌─────────────────┐  ┌─────────────────────────┐   │
│  │ 通义千问 (云端)  │  │ Ollama (本地)            │   │
│  │ • qwen-max      │  │ • qwen2.5:7b            │   │
│  │ • qwen-turbo    │  │ • deepseek-r1:8b        │   │
│  └─────────────────┘  └─────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

### 数据流示意

```
用户输入 → Prompt Template → 模型推理 → Output Parser → 结构化输出
    ↓                                                              ↓
[会话历史] ← Memory 存储 ← 中间结果记录 ← [链式组合 Chain]
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

### Q1: 如何获取通义千问 API Key？

**A**: 
1. 访问 [阿里云百炼平台](https://bailian.console.aliyun.com/)
2. 注册/登录阿里云账号
3. 进入「API-KEY 管理」页面
4. 创建新的 API Key 并复制

### Q2: Ollama 启动失败怎么办？

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

### Q3: 出现 502 错误如何解决？

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

### Q4: 内存不足怎么处理？

**A**: 
- 减小模型规模：使用 `qwen2.5:3b`（约 2GB）代替 `qwen2.5:7b`
- 关闭其他占用内存的程序
- 增加 swap 空间（Linux）或虚拟内存（Windows）

### Q5: 如何切换使用不同的模型？

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

Week 7+: 高级应用
├── 集成外部工具和 API
├── 实现 RAG 检索增强生成
└── 开发完整的 Agent 应用
```

---

## 🙏 致谢

- **LangChain 团队** - 提供强大的 AI 应用开发框架
- **阿里云** - 提供通义千问大模型服务
- **Ollama** - 让本地运行大模型变得简单
- **Qwen 团队** - 开源优秀的中文大模型
- **黑马程序员** - 提供免费的教学视频

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

