__author__ = 'alberick'
# Twitter Web Services

import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

tweets = api.search('#python')

for tweet in tweets:
    print tweet.created_at, tweet.text, '\n'