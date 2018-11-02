from mastodon import Mastodon
import urllib.request

mastodon = Mastodon(
    access_token = 'whatthecommit.secret',
    api_base_url = 'https://botsin.space'
)

commit = urllib.request.urlopen('https://whatthecommit.com/index.txt').read().decode('utf-8').rstrip()


mastodon.status_post("\"" + commit +"\"")
