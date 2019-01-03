import tweepy
import json
import os, random, sys

envroot = '/cluster/home/cjearley13/cooltreepix/'
filepath = envroot + 'credentials.json'
imagedir = envroot + "sources/"
tweeteddir = envroot + "tweeted/"

with open(filepath) as data_file:
    data = json.load(data_file)

consumer_key = data['consumer_key']
consumer_secret =  data['consumer_secret']
access_token = data['access_token']
access_token_secret = data['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

status = ""

if not os.listdir(imagedir):
	print("empty directory, get more pictures")
	sys.exit()

currentimage = random.choice(os.listdir(imagedir))

imagepath = imagedir + currentimage

# Send the tweet.
api.update_with_media(imagepath, status)

# store the tweeted image so it isn't repeated
tweetedimagepath = tweeteddir + currentimage
#os.rename(selectedimagepath,tweetedimagepath)
