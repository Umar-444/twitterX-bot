import tweepy
import os
import random
import time
from datetime import datetime, timedelta

# Load credentials from environment variables
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_KEY_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
api = tweepy.API(auth)

# Tweets list
tweets = [
    "Good morning! Testing my Twitter bot.",
    "Learning Python automation with Tweepy.",
    "Posting automatically using Railway and Twitter API!",
    "This is another automated post by my bot.",
    "Building my developer skills with daily posting."
]

# Function to post a tweet
def post_tweet():
    tweet = random.choice(tweets)
    api.update_status(tweet)
    print(f"[{datetime.now()}] Posted: {tweet}")

# Post 3 tweets per day
while True:
    for i in range(3):
        post_tweet()
        time.sleep(8 * 60 * 60)  # Wait 8 hours between tweets
    # Wait until the next day
    time.sleep(24 * 60 * 60)
