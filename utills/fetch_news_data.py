import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('news_api_key') 

def fetch_news(coin):
    base_url = "https://newsdata.io/api/1/latest"
    
    params = {
        "apikey": api_key,
        "q": coin,
        "language": "en"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return {}


# news_data = fetch_news("cryptocurrency")

# if news_data and "results" in news_data:
#     for article in news_data["results"]:
#         print(f"Title: {article.get('title')}")
#         print(f"Snippet: {article.get('description')}")
#         print(f"URL: {article.get('link')}")
#         print("-" * 50)
# else:
#     print("No news articles found.")



# base_url = " https://newsdata.io/api/1/latest?apikey=pub_3ccab72e01964b19b8998d058d86f9c0&q={Bitcoin}"  # ← This is the correct endpoint for NewsData.io
# parameters = {
#     "api": api_key,
#     "q": "cryptocurrency",
#     "language": "en"
# }

# try:
#     response = requests.get(base_url)
#     response.raise_for_status()  # Raise an exception for bad status codes
#     news_data = response.json()

#     for article in news_data.get("results", []):
#         print(f"Title: {article.get('title')}")
#         print(f"Snippet: {article.get('description')}")
#         print(f"URL: {article.get('link')}\n")

# except requests.exceptions.RequestException as e:
#     print(f"Error fetching news: {e}")