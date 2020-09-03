import requests
import pandas as pd
from bs4 import BeautifulSoup


url = 'https://ca.octobersveryown.com/collections/all?page={page}&view=pagination-ajax'

page = 1
all_data = []
while True:
    soup = BeautifulSoup( requests.get(url.format(page=page)).content, 'html.parser' )

    li = soup.find_all('li', recursive=False)
    if not li:
        break

    for l in li:
        d = {'name': l.select_one('p a').get_text(strip=True),
             'link': 'https:' + l.img['src'],
             'price': l.select_one('.grid-price').get_text(strip=True, separator=' ')}
        all_data.append(d)
        print(d)
        print('-' * 80)

    page += 1

df = pd.DataFrame(all_data)
df.to_csv('data.csv')
print(df)