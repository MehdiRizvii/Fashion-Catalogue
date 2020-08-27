import requests
from bs4 import BeautifulSoup

url = 'https://ca.octobersveryown.com/collections/all'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

bodies = (soup.find(id='content'))

clothing = bodies.find_all("ul", "grid--full product-grid-items")
for span_tag in soup.findAll('span', 'visually-hidden'):
    span_tag.replace_with('')

print(clothing[0].find('img')['src'])
print(clothing[0].find("p", 'product-title').get_text())
print(clothing[0].find("span", 'grid-price-money').get_text())

