from utills.fetch_tweets_data import fetch_tweets
from models.main_agent import run_local_llm

def analyze_tweets(coin="bitcoin"):
    tweets = fetch_tweets(coin)
    prompt = f"""Analyze the sentiment about {coin} using following sentiments regarding it
                 followers_count: Total number of followers of associated X accounts.
                 tweets_count: Total number of tweets and retweets made by associated X accounts.
                 listed_count: Number of lists the X account is a member of.
                 favorite_count: Total number of tweets favorited by the X account.
                 And other related metrics.:\n\n""" + "\n".join(tweets)
    return run_local_llm(prompt)
