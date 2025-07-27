# import requests
from models.main_agent import run_local_llm

# def get_price_data(symbol="BTCUSDT", interval="1h", limit=50):
#     return f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    

# def analyze_price(symbol="BTCUSDT"):
#     data = get_price_data(symbol=symbol)
#     print(data)
#     table = "\n".join([f"{row['open']}, {row['high']}, {row['low']}, {row['close']}" for row in data])

import hmac
import hashlib
import time
import requests
from urllib.parse import urlencode
import os
from dotenv import load_dotenv

load_dotenv()
# ✅ Get API credentials from environment variables
api_key = os.getenv("api_key")
api_secret = os.getenv("api_secret")

# ✅ Correct base URL
base_url = 'https://api.binance.com'

# ✅ Function to create a signature for authenticated endpoints
def get_signature(query_string):
    return hmac.new(
        api_secret.encode('utf-8'),
        query_string.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

# ✅ Example request to get account information
def get_account():
    endpoint = '/api/v3/account'
    timestamp = int(time.time() * 1000)

    params = {
        'timestamp': timestamp,
        'recvWindow': 5000  # Optional parameter
    }

    query_string = urlencode(params)
    signature = get_signature(query_string)

    url = f"{base_url}{endpoint}?{query_string}&signature={signature}"

    headers = {
        'X-MBX-APIKEY': api_key
    }

    response = requests.get(url, headers=headers)
    return response.json()

# import requests
# from models.main_agent import run_local_llm

# def get_price_data(symbol="BTCUSDT", interval="1h", limit=50):
#     return f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    

# def analyze_price(symbol="BTCUSDT"):
#     data = get_price_data(symbol=symbol)
#     print(data)
#     table = "\n".join([f"{row['open']}, {row['high']}, {row['low']}, {row['close']}" for row in data])

def get_order_book(symbol, limit=100):
    endpoint = '/api/v3/depth'
    params = {
        'symbol': symbol,
        'limit': limit
    }
    url = f"{base_url}{endpoint}?{urlencode(params)}"
    response = requests.get(url)
    return response.json()

# Get recent trades
def get_recent_trades(symbol, limit=500):
    endpoint = '/api/v3/trades'
    params = {
        'symbol': symbol,
        'limit': limit
    }
    url = f"{base_url}{endpoint}?{urlencode(params)}"
    response = requests.get(url)
    return response.json()

# Get candlestick data
def get_klines(symbol, interval, start_time=None, end_time=None, limit=500):
    endpoint = '/api/v3/klines'
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': limit
    }

    if start_time:
        params['startTime'] = start_time
    if end_time:
        params['endTime'] = end_time

    url = f"{base_url}{endpoint}?{urlencode(params)}"
    response = requests.get(url)

    # Format the response
    klines = response.json()
    formatted_klines = []
    for k in klines:
        formatted_klines.append({
            'open_time': k[0],
            'open': float(k[1]),
            'high': float(k[2]),
            'low': float(k[3]),
            'close': float(k[4]),
            'volume': float(k[5]),
            'close_time': k[6],
            'quote_volume': float(k[7]),
            'trades': k[8],
            'taker_buy_base_volume': float(k[9]),
            'taker_buy_quote_volume': float(k[10])
        })

    return formatted_klines

