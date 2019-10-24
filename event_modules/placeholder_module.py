import requests
import urllib.request
import time
from bs4 import BeautifulSoup


# FIXME: @FynnGrandke URL needs to be adjustable
def meetup():
    # TODO: Insert URL where to fetch from
    url = ''

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    # TODO: Name, date, time of event
    for tag in soup.findAll('span', {'itemprop': 'name'}):
        print('Meetup' + tag.string)
