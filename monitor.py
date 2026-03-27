from llm_chain import get_monitor_chain
from config import OUTPUT_MONITOR_REPORT

monitor_chain = get_monitor_chain()

def run_monitor(df_analyzed):
    summary = df_analyzed.to_string(index=False)

    print("\n正在生成竞品监控与价格预警报告...")
    report = monitor_chain.invoke({"goods_summary": summary})

    with open(OUTPUT_MONITOR_REPORT, "w", encoding="utf-8") as f:
        f.write("===== 电商竞品监控 & 价格预警报告 =====\n\n")
        for key, value in report.items():
            f.write(f"【{key}】\n{value}\n\n")

    print("\n===== 报告输出完成 =====")
    for k, v in report.items():
        print(f"\n【{k}】\n{v}")

    return report