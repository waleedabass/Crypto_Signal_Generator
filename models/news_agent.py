from utills.fetch_news_data import fetch_news
from models.main_agent import run_local_llm

def analyze_news(coin):
    headlines = fetch_news(coin)
    prompt = f"""Summarize the sentiment of the following crypto news headlines about {coin}:\n\n""" + "\n".join(headlines)
    return run_local_llm(prompt)
