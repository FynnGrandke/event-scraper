import requests
import urllib.request
import time
from bs4 import BeautifulSoup


# FIXME: @FynnGrandke URL needs to be adjustable
# TODO: Replace module name
def getPLACEHOLDEREvent():
    # TODO: Insert URL where to fetch from
    url = 'PLACEHOLDER'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    # TODO: Name, date, time of event
    for tag in soup.findAll('HTMLELEMENT', {'PROPERTY': 'NAME'}):
        print('PLACEHOLDER: ' + tag.string)
