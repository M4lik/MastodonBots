from mastodon import Mastodon
import time
import datetime
import urllib.request

mastodon = Mastodon(
    access_token = 'waitingforc3.secret',   # File for "Your access token", can be created unter "Settings" -> "Development" -> "Your applications"
    api_base_url = 'https://botsin.space'   # URL that the bot is hosted on
)

_today = datetime.date.today()
theDay = datetime.date(_today.year, 12, 27)
Dez28 = datetime.date(_today.year, 12, 28)
Dez29 = datetime.date(_today.year, 12, 29)
Dez30 = datetime.date(_today.year, 12, 30)
Dez31 = datetime.date(_today.year, 12, 31)
hashtag = "#" + str(_today.year - 1983) + "C3"      # Hasthag of this years C3
nextHashtag = "#" + str(_today.year - 1982) + "C3"  # Hashtag of next years C3
stringList = urllib.request.urlopen("https://raw.githubusercontent.com/t-aus-m/MastodonBots/testing/announcements.txt").read().decode('utf-8').splitlines()
daysUntiltheDay = (theDay - _today).days

if theDay == _today :
    # Post for 1st day of C3
    print()
elif Dez28 == _today :
    # Post for 2nd day of C3
    print()
elif Dez29 == _today :
    # Post for 3rd day of C3
    print()
elif Dez30 == _today :
    # Post for 4th and last day of C3
    print()
elif Dez31 == _today :
    # Post for day after C3
    print()
else :
    # Post for every other day
    print(stringList)
