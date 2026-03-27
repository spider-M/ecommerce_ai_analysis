import os
from langchain_openai import ChatOpenAI

# ==================== 从系统环境变量读取 API KEY ====================
LLM_MODEL = "qwen3-max"
API_KEY = os.getenv("DASHSCOPE_API_KEY")  # 从系统变量读取
BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"

# 初始化LLM
def get_llm():
    return ChatOpenAI(
        model=LLM_MODEL,
        api_key=API_KEY,
        base_url=BASE_URL,
        temperature=0.1
    )

# ==================== 文件路径 ====================
INPUT_EXCEL = "goods_data.xlsx"
OUTPUT_BATCH_RESULT = "商品批量AI分析结果.xlsx"
OUTPUT_MONITOR_REPORT = "电商竞品监控预警报告.txt"