from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from config import get_llm

llm = get_llm()

# ==================== 商品结构化清洗 ====================
def get_item_chain():
    schema = [
        ResponseSchema(name="standard_name", description="标准商品名"),
        ResponseSchema(name="brand", description="品牌"),
        ResponseSchema(name="category", description="品类"),
        ResponseSchema(name="price_level", description="低/中/高"),
        ResponseSchema(name="sales_level", description="高/中/低"),
        ResponseSchema(name="competitive", description="强/中/弱"),
        ResponseSchema(name="is_hot", description="是/否"),
    ]
    parser = StructuredOutputParser.from_response_schemas(schema)
    format_instr = parser.get_format_instructions()

    prompt = PromptTemplate(
        template="""
你是电商数据专家，结构化解析商品信息，只返回JSON。
标题：{title}
价格：{price}
销量：{sales}

{format_instructions}
""",
        input_variables=["title", "price", "sales"],
        partial_variables={"format_instructions": format_instr}
    )
    return prompt | llm | parser

# ==================== 竞品监控 & 价格预警 ====================
def get_monitor_chain():
    schema = [
        ResponseSchema(name="brand_competition", description="品牌竞争格局"),
        ResponseSchema(name="price_warning", description="价格风险预警"),
        ResponseSchema(name="hot_rank", description="爆款TOP与特征"),
        ResponseSchema(name="competitor_warning", description="竞品危险行为"),
        ResponseSchema(name="business_strategy", description="企业运营策略"),
        ResponseSchema(name="risk_hint", description="风险提示")
    ]
    parser = StructuredOutputParser.from_response_schemas(schema)
    format_instr = parser.get_format_instructions()

    prompt = PromptTemplate(
        template="""
你是资深电商战略分析师，基于商品数据做竞品监控与价格预警。

商品数据：
{goods_summary}

输出6项内容：品牌格局、价格预警、爆款TOP、竞品危险行为、企业策略、风险提示。

{format_instructions}
""",
        input_variables=["goods_summary"],
        partial_variables={"format_instructions": format_instr}
    )
    return prompt | llm | parser