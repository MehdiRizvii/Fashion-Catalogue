import requests
import json
from bs4 import BeautifulSoup

url = 'https://ca.octobersveryown.com/collections/all'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

clothing = (soup.find_all(id='content'))

print(clothing)

print(clothing.find_all('li'))
