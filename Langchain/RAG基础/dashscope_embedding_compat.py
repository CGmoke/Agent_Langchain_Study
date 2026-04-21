# -*- coding: utf-8 -*-
"""
DashScope 文本嵌入模型 - 兼容版
解决 langchain-community 与新版 DashScope SDK (v1.25+) 的兼容性问题
"""

import sys
import os
from typing import List, Optional
from langchain_core.embeddings import Embeddings


class DashScopeEmbeddingCompat(Embeddings):
    """
    兼容版 DashScope 嵌入模型
    
    直接使用 dashscope SDK，绕过 langchain-community 的兼容性问题
    支持 text-embedding-v1/v2/v3 所有版本
    """

    def __init__(
        self,
        model: str = "text-embedding-v2",
        api_key: Optional[str] = None,
        **kwargs
    ):
        """
        初始化嵌入模型
        
        参数:
            model: 模型名称 (text-embedding-v1/v2/v3)
            api_key: DashScope API Key
        """
        self.model = model
        
        # 获取 API Key
        if not api_key:
            api_key = os.getenv("DASHSCOPE_API_KEY", "")
        
        if not api_key or not api_key.strip():
            raise ValueError(
                "未提供有效的 DashScope API Key。\n"
                "请通过以下任一方式配置:\n"
                "  1. 构造函数传入: DashScopeEmbeddingCompat(api_key='your-key')\n"
                "  2. 设置环境变量: DASHSCOPE_API_KEY=your-key"
            )
        
        self.api_key = api_key.strip()
        
        # 导入 dashscope SDK
        try:
            from dashscope import TextEmbedding
            self._TextEmbedding = TextEmbedding
        except ImportError:
            raise ImportError("请安装 dashscope 库: pip install dashscope")

    def _embed_batch(self, texts: List[str]) -> List[List[float]]:
        """批量嵌入文本"""
        # 调用 DashScope SDK (已验证可正常工作)
        resp = self._TextEmbedding.call(
            model=self.model,
            input=texts,  # 必须是列表格式
            api_key=self.api_key
        )
        
        if resp.status_code == 200:
            return [item["embedding"] for item in resp.output["embeddings"]]
        else:
            raise ValueError(f"API 错误 {resp.status_code}: {resp.message} (code: {resp.code})")

    def embed_query(self, text: str) -> List[float]:
        """嵌入单个查询文本"""
        # 处理 LangChain 可能传入的非字符串类型（如 dict）
        if isinstance(text, dict):
            # 从 dict 中提取实际的查询文本
            text = text.get("input", text.get("query", str(text)))
        if not isinstance(text, str):
            text = str(text)
        return self._embed_batch([text])[0]

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """嵌入多个文档文本"""
        if not texts:
            return []
            
        all_embeddings = []
        batch_size = 6  # 批次大小
        
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            
            try:
                embeddings = self._embed_batch(batch)
                all_embeddings.extend(embeddings)
                
            except Exception as e:
                if len(batch) > 1:
                    # 单个重试
                    for text in batch:
                        try:
                            emb = self._embed_batch([text])
                            all_embeddings.extend(emb)
                        except Exception as inner_e:
                            raise ValueError(f"嵌入文本失败: {inner_e}")
                else:
                    raise e
        
        return all_embeddings

    def __repr__(self) -> str:
        return f"DashScopeEmbeddingCompat(model='{self.model}')"


# 测试代码
if __name__ == "__main__":
    print("=" * 60)
    print("DashScope 兼容版嵌入模型测试")
    print("=" * 60)
    
    try:
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from qwen_api_key import get_qwen_api_key
        
        embedding = DashScopeEmbeddingCompat(
            model="text-embedding-v2",
            api_key=get_qwen_api_key()
        )
        
        print(f"\n[TEST] 嵌入测试文本...")
        vec = embedding.embed_query("你好世界")
        print(f"[OK] 向量维度: {len(vec)}")
        print(f"[SUCCESS] 测试通过！")
        
    except Exception as e:
        print(f"[ERROR] {type(e).__name__}: {e}")
