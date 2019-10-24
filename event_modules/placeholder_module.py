import requests
import urllib.request
import time
from bs4 import BeautifulSoup

def meetup():
  url = ''

  response = requests.get(url)

  soup = BeautifulSoup(response.text, "html.parser")

  for tag in soup.findAll('span', {'itemprop': 'name'}):
    print(tag.string)