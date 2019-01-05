import tweepy
import json
import os, random, sys, subprocess
import argparse

DEBUG = False

# a file of up to 3072KB can be uploaded to Twitter, max size is rounded down (unit is bytes)
MAXFILESIZE=3000000

envroot = '/cluster/home/cjearley13/cooltreepix/'
filepath = envroot + 'credentials.json'
imagedir = envroot + "sources/"
tweeteddir = envroot + "tweeted/"

with open(filepath) as cred_file:
    credential = json.load(cred_file)

consumer_key = credential['consumer_key']
consumer_secret =  credential['consumer_secret']
access_token = credential['access_token']
access_token_secret = credential['access_token_secret']

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", help="debug mode", action="store_true")
parser.add_argument("-i", "--image", help="tweet given image", action="store")
args = parser.parse_args()
DEBUG = args.debug

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

status = ""

if not os.listdir(imagedir):
	print("empty directory, get more pictures")
	sys.exit()

if (args.image) and (os.path.isfile(imagedir + args.image)):
	currentimage = args.image
else:
	currentimage = random.choice(os.listdir(imagedir))

imagepath = imagedir + currentimage

if (DEBUG):
	print(imagepath)

imagesize = os.path.getsize(imagepath)
if (imagesize > MAXFILESIZE):
	percentage = float(MAXFILESIZE) / float(imagesize) * 100.0
	resize_command = '/usr/bin/convert -resize ' + str(percentage) + '% ' + imagepath + ' ' + imagepath
	if (DEBUG):
		print(imagepath + " is too large, trying to resize...")
		print(resize_command)
	subprocess.call(resize_command, shell=True)

# everything after this should only happen as part of production
if (DEBUG):
	sys.exit()

# Send the tweet.
api.update_with_media(imagepath, status)

# store the tweeted image so it isn't repeated
tweetedimagepath = tweeteddir + currentimage
os.rename(imagepath,tweetedimagepath)
