from batch_analyzer import run_batch_analyze
from monitor import run_monitor

if __name__ == "__main__":
    # 1. 批量分析商品
    analyzed_df = run_batch_analyze()

    # 2. 竞品监控 + 价格预警
    run_monitor(analyzed_df)