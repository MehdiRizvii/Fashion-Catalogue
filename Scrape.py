import requests
from bs4 import BeautifulSoup
page = requests.get('https://api.louisvuitton.com/api/eng-ca/catalog/filter/epy4e8?range=0-50')

soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
