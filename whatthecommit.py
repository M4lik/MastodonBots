#!/usr/bin/python3

from mastodon import Mastodon
import urllib.request

mastodon = Mastodon(
    access_token = 'whatthecommit.secret',  # File for "Your access token", can be created unter "Settings" -> "Development" -> "Your applications"
    api_base_url = 'https://botsin.space'   # URL that the bot is hosted on
)

commit = urllib.request.urlopen('https://whatthecommit.com/index.txt').read().decode('utf-8').rstrip()


mastodon.status_post("\"" + commit +"\"")
