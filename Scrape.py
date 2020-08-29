import requests
from bs4 import BeautifulSoup


url = 'https://uk.octobersveryown.com/collections/all?page={page}&view=pagination-ajax'

page = 1
while True:
    soup = BeautifulSoup( requests.get(url.format(page=page)).content, 'html.parser' )

    li = soup.find_all('li', recursive=False)
    if not li:
        break

    for l in li:
        print(l.select_one('p a').get_text(strip=True))
        print('https:' + l.img['src'])
        print(l.select_one('.grid-price').get_text(strip=True, separator=' '))
        print('-' * 80)

    page += 1