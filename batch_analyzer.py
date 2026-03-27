import pandas as pd
import time
from llm_chain import get_item_chain
from config import INPUT_EXCEL, OUTPUT_BATCH_RESULT

chain = get_item_chain()

def run_batch_analyze():
    df = pd.read_excel(INPUT_EXCEL, engine="openpyxl")
    result = []

    print(f"开始批量分析商品总数：{len(df)}")

    for i, row in df.iterrows():
        try:
            title = str(row["商品标题"])
            price = str(row["商品价格"])
            sales = str(row["销量"])

            ai_data = chain.invoke({
                "title": title,
                "price": price,
                "sales": sales
            })

            result.append({
                "平台": row["平台"],
                "原始标题": title,
                "价格": price,
                "销量": sales,
                "店铺": row["店铺名称"],
                "标准名称": ai_data["standard_name"],
                "品牌": ai_data["brand"],
                "品类": ai_data["category"],
                "价格档次": ai_data["price_level"],
                "销量等级": ai_data["sales_level"],
                "竞争力": ai_data["competitive"],
                "是否爆款": ai_data["is_hot"],
            })

            if i % 10 == 0:
                print(f"已完成：{i} 条")

            time.sleep(0.2)

        except Exception as e:
            print(f"第{i}条失败：{e}")
            continue

    df_out = pd.DataFrame(result)
    df_out.to_excel(OUTPUT_BATCH_RESULT, index=False)
    print(f"\n✅ 批量分析完成：{OUTPUT_BATCH_RESULT}")
    return df_out