#!/usr/bin/python3

import random
import tweepy
from credentials import *
from compliments import *
from time import sleep

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def complimenter():
    adjective1 = random.choice(adjectives)
    adjective2 = random.choice(adjectives)
    noun = random.choice(nouns)
    compliment = 'Ann, you {}, {} {}!'.format(adjective1, adjective2, noun)
    return compliment

def main():
    line = complimenter()
    #print(line)
    api.update_status(line)

if __name__ == "__main__":
  main()