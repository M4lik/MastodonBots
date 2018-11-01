from mastodon import Mastodon
import time
import datetime

mastodon = Mastodon(
    access_token = 'waitingforc3.secret',
    api_base_url = 'https://botsin.space'
)

_today = datetime.date.today()
theDay = datetime.date(_today.year, 12, 27)
Dez28 = datetime.date(_today.year, 12, 28)
Dez29 = datetime.date(_today.year, 12, 29)
Dez30 = datetime.date(_today.year, 12, 30)
Dez31 = datetime.date(_today.year, 12, 31)
hashtag = "#" + str(_today.year - 1983) + "C3"
nextHashtag = "#" + str(_today.year - 1982) + "C3"

daysUntiltheDay = (theDay - _today).days

if theDay == _today :
    mastodon.status_post("Today is the day! 0 Days until " + hashtag + "! \nHave a very excellent Chaos Communication Congress. \\o/")
elif Dez28 == _today :
    mastodon.status_post("It's the second day of " + hashtag + ". \nLet's light up all the LEDs and make all the network cables glow!")
elif Dez29 == _today :
    mastodon.status_post("The third day of " + hashtag + " is in full progress.\nDrink all the mate and don't forget to wash your hands!")
elif Dez30 == _today :
    mastodon.status_post("The fourth and final day of the " + hashtag + "has begun. \nLet's party hack hard and party harder!")
elif Dez31 == _today :
    mastodon.status_post("That was " + hashtag + "! What a blast! \nA good and save way home to everyone. See you at " + nextHashtag + "!")
else :
    mastodon.status_post("We are happy to announce that there are only " + str(daysUntiltheDay) + " Days left until " + hashtag + "!")