# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "PAmpYOq5LwscMnRSFBQqwNjxH"
consumer_secret = "uvvEfLcCoU9zBsRwc3wbWNGwUy7BUVtYH3376MHpLDy7oZ6qUK"
access_token = "907734237478080523-BAtPF5z8EzzwyPef0f04JC12LOQSCim"
access_token_secret = "0F5xIDmAwVAy7pQcOWs0mMFDedr9po1tLJuLNk8r3gMuG"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
def TweetOut(tweet_number):
    api.update_status(
        "Can't stop. Won't stop. Chatting! This is Tweet #%s!" %
        tweet_number)


# Create a function that calls the TweetOut function every minute
counter = 0

# Infinitely loop
while(True):

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(60)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1