import requests
import urllib.request
import time
from bs4 import BeautifulSoup


# FIXME: @FynnGrandke URL needs to be adjustable
def getAlleventsinEvents():
    url = 'https://allevents.in/tokyo/?ref=home-page'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    # TODO: Fix bug with concatenating string
    for tag in soup.findAll('h3'):
        print('eventsin: ' + tag.string)
