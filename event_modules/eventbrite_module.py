import requests
import urllib.request
import time
from bs4 import BeautifulSoup


# FIXME: @FynnGrandke URL needs to be adjustable
def getEventbriteEvents():
    # TODO: Insert URL where to fetch from
    url = 'https://www.eventbrite.ca/d/japan--tokyo/all-events/?start_date=2019-10-31&end_date=2019-11-01&page=1'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    # TODO: Name, date, time of event
    for tag in soup.findAll('div', {'data-spec': 'event-card__formatted-name--content'}):
        print('Eventbrite: ' + tag.string)
