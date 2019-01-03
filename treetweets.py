import tweepy
import json
import os, random, sys, subprocess

# a file of up to 3072KB can be uploaded to Twitter, max size is rounded down (unit is bytes)
MAXFILESIZE=3000000

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

imagesize = os.path.getsize(imagepath)
if (imagesize > MAXFILESIZE):
	percentage = MAXFILESIZE / imagesize * 100
	resize_command = '/usr/bin/convert -resize ' + percentage + '% ' + imagepath + ' ' + imagepath
	subprocess.call(cmd, shell=True)

# Send the tweet.
api.update_with_media(imagepath, status)

# store the tweeted image so it isn't repeated
tweetedimagepath = tweeteddir + currentimage
#os.rename(selectedimagepath,tweetedimagepath)
