import requests
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_tweets(asset_symbol):
    """
    Fetches significant asset events from CoinDesk API for a given symbol (e.g., BTC, ETH).
    """
    api_key = os.getenv('COINDESK_API_KEY')
    if not api_key:
        print("Error: COINDESK_API_KEY not found in .env file.")
        return None

    base_url = "https://data-api.coindesk.com/asset/v1/events"
    params = {
        "asset": asset_symbol,
        "asset_lookup_priority": "SYMBOL"
    }

    headers = {
        "x-api-key": api_key
    }

    try:
        response = requests.get(base_url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching events: {e}")
        if e.response is not None:
            print(f"Details: {e.response.text}")
        return None
    

# if __name__ == "__main__":
#     # Ensure your .env file has a line like:
#     # COINDESK_API_KEY="YOUR_ACTUAL_COINDESK_API_KEY_HERE"

#     # Example Usage:
#     crypto_asset = "BTC" # Bitcoin
#     # Fetch data for the last 7 days ending yesterday
#     end_date = datetime.date.today() - datetime.timedelta(days=1)
#     num_days = 7

#     print(f"Fetching X data for {crypto_asset} for the last {num_days} days until {end_date}...")
#     twitter_data = get_coindesk_twitter_data(crypto_asset, limit=num_days, to_date=end_date)

#     if twitter_data and twitter_data.get("Data"): # Data is usually nested under "Data" or "results" key
#         print("\n--- CoinDesk X Data ---")
#         for entry in twitter_data["Data"]: # Or twitter_data["data"] based on exact JSON structure
#             date_ts = entry.get("time") # This might be a Unix timestamp
#             # Convert timestamp to human-readable date if 'time' is a timestamp
#             if date_ts:
#                 date_obj = datetime.datetime.fromtimestamp(date_ts).strftime('%Y-%m-%d')
#             else:
#                 date_obj = "N/A"

#             print(f"Date: {date_obj}")
#             print(f"  Total Tweets: {entry.get('tweets_count')}")
#             print(f"  Total Followers: {entry.get('followers_count')}")
#             print(f"  Favorited Count: {entry.get('favorite_count')}")
#             print("-" * 20)
#     elif twitter_data:
#         print("No 'Data' found in the response, or response is empty.")
#         print(twitter_data) # Print full response to inspect structure
#     else:
#         print("Failed to retrieve CoinDesk X data.")

    # You might want to try other assets:
    # crypto_asset_eth = "ETH"
    # twitter_data_eth = get_coindesk_twitter_data(crypto_asset_eth, limit=5)
    # if twitter_data_eth:
    #     print(f"\n--- CoinDesk X Data for ETH ---")
    #     # Process ETH data similarly





# import subprocess

# def fetch_tweets(coin="bitcoin"):
#     # Construct the proper search query
#     search_query = f"{coin} since:2023-07-01 until:2025-07-24"
#     cmd = f"snscrape --max-results 30 twitter-search \"{search_query}\""

#     try:
#         result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
#         tweets = result.stdout.split('\n')
#         return [line for line in tweets if line]
#     except Exception as e:
#         print(f"Error running snscrape: {e}")
#         return []

# # Example usage
# tweets = fetch_tweets("ethereum")
# for t in tweets[:5]:  # print top 5 tweet lines
#     print(t)

