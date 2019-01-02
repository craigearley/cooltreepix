import tweepy
import json

with open('credentials.json') as data_file:
    data = json.load(data_file)

consumer_key = data['consumer_key']
consumer_secret =  data['consumer_secret']
access_token = data['access_token']
access_token_secret = data['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

image = "IMAG0245.jpg"
status = ""

# Send the tweet.
api.update_with_media(image, status)
