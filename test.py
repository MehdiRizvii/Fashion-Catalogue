import requests
import pandas as pd
from bs4 import BeautifulSoup


url = 'https://www.stussy.com/collections/mens-new-arrivals?page={page}&view=pagination-ajax'

page = 1
all_data = []
while True:
    soup = BeautifulSoup( requests.get(url.format(page=page)).content, 'html.parser' )

    li = soup.find_all('li', recursive=False)
    if not li:
        break

    for l in li:
        d = {'link': '<img src="' 'https:' + l.img['src'] + '">',
             'name': l.select_one('p a').get_text(strip=True),
             'price': l.select_one('.product-card__price').get_text(strip=True, separator=' ')}
        all_data.append(d)
        print(d)
        print('-' * 80)

    page += 1
