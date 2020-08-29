from selenium import webdriver
from bs4 import BeautifulSoup
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://ca.octobersveryown.com/collections/all")

scrolls = 22
while True:
    scrolls -= 1
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(0.2)
    if scrolls < 0:
        break

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

bodies = (soup.find(id='content'))

clothing = bodies.find_all(class_='grid--full product-grid-items')
for span_tag in soup.findAll(class_='visually-hidden'):
    span_tag.replace_with('')

print(clothing[0].find('img')['src'])
print(clothing[0].find(class_='product-title').get_text())
print(clothing[0].find(class_='grid-price-money').get_text())

time.sleep(8)

driver.quit()

