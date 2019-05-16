#!/usr/bin/python3

import urllib.request
from bs4 import BeautifulSoup
import time as _time
import pickle
from mastodon import Mastodon
import os
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))
mastodon = Mastodon(
    access_token = 'stoerungsmelder.secret',   # File for "Your access token", can be created unter "Settings" -> "Development" -> "Your applications"
    api_base_url = 'https://botsin.space'   # URL that the bot is hosted on
)
lastTootTime = 0

class tweet:
    def time(self):
        return int(self.tweet.find('span', attrs={'class','_timestamp'})['data-time'])

    def content(self):
        return self.tweet.find('p', attrs={'class','tweet-text'}).text

    def media(self):
        media = self.tweet.find_all('div', attrs={'class', 'AdaptiveMedia-photoContainer'})
        for i in range(len(media)):
            media[i] = media[i]['data-image-url']
        return media

    def success(self):
        return True if type(self.tweet) == type(BeautifulSoup('<b/>',features="html.parser").b) else False

    def __init__(self, body):
        self.tweet = body

def tweetTooter(thisTweet):
    global lastTootTime
    nextTweet = tweet(thisTweet.tweet.find_next('div', attrs={'class':'tweet'}))
    if thisTweet.success() and lastTootTime < thisTweet.time():
        tweetTooter(nextTweet)
        if not thisTweet.media:
            mastodon.status_post(thisTweet.content())
        else:
        lastTootTime = thisTweet.time()
    else:
        return


if __name__ == "__main__":
    URL = 'https://twitter.com/stoerungsmelder'
    twitter = urllib.request.urlopen(URL).read().decode('utf-8').rstrip()
    parsed_html = BeautifulSoup(twitter, features="html.parser")
    firstTweet = tweet(parsed_html.body.find('div', attrs={'class':'tweet'}))
    print(type(firstTweet.media()))
    '''
    try:
        lastTootTime = pickle.load(open("./lastTootTime.log", 'rb'))
    except:
        print("Time-file does not exist. Creating one.")
        lastTootTime = _time.time()
        pickle.dump(lastTootTime, open("./lastTootTime.log", 'wb'))

    tweetTooter(firstTweet)
    pickle.dump(lastTootTime, open("./lastTootTime.log", 'wb'))
    '''
