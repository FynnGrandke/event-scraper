import requests
import urllib.request
import time
from bs4 import BeautifulSoup


def meetup():
    # FIXME: @FynnGrandke URL needs to be adjustable
    url = 'https://www.meetup.com/find/events/?allMeetups=true&radius=25&userFreeform=Tokyo%2C+Japan&mcId=c1023444&mcName=Tokyo%2C+JP&month=10&day=19&year=2019'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup.findAll('span', {'itemprop': 'name'}):
        print('Meetup: ' + tag.string)
