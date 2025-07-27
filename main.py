from models.price_agent import analyze_price
from utills.fetch_news_data import fetch_news
from utills.fetch_tweets_data import fetch_tweets
from models.fusion_agent import fusion_analysis
import streamlit as st
from models.price_agent import analyze_price
from utills.fetch_news_data import fetch_news
from utills.fetch_tweets_data import fetch_tweets
from models.fusion_agent import fusion_analysis  # Your fusion logic

st.set_page_config(page_title="Crypto Trade Signal", layout="centered")

# Title
st.title("📈 Crypto Trade Signal Generator")

st.markdown("Enter a crypto symbol (e.g., `BTC`, `ETH`, `RENDER`) to get a signal.")
coin = st.text_input("Enter coin symbol:", value="BTC").upper()

st.markdown("Enter a time interval for analysis of coin e.g., 1m,1s,1h or 1W,1M,... (Optional) ")
interval=st.text_input(":", value="1w")
# Trigger analysis
if st.button("🔍 Analyze Now"):
    with st.spinner("Fetching data and analyzing..."):
        price = analyze_price(interval,coin)
        news = fetch_news(coin)
        tweets = fetch_tweets(coin)

        result = fusion_analysis(coin, price, news, tweets)

    if result.startswith("Error"):
        st.error("❌ Something went wrong while generating the trade signal.")
        st.code(result, language="text")
    else:
        st.success("✅ Trade Signal Generated!")
        st.markdown("### 📋 Signal Output")
        st.markdown(result)

