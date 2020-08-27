import requests
from bs4 import BeautifulSoup

url = 'https://ca.octobersveryown.com/collections/all'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

bodies = (soup.find(id='content'))

clothing = bodies.find_all("ul", "grid--full product-grid-items")

print(clothing)


