from utills.fetch_price_data import get_klines
from models.main_agent import run_local_llm

def analyze_price(interval,coin="BTC"):
    data = get_klines(f"{coin}USDT",interval)
    table = "\n".join([f"{row['open']}, {row['high']}, {row['low']}, {row['close']}" for row in data])
    prompt = f"""You are a crypto analyst. Analyze the following price history and classify the trend as bullish, bearish, or neutral:\n\n{table}"""
    return run_local_llm(prompt)
