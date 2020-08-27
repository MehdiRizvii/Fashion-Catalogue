
start = 0
finish = 50
url = f'https://api.louisvuitton.com/api/eng-ca/catalog/filter/epy4e8?range={start}-{finish}'
while True:
    print(url)
    if True:
        start += 50
        finish += 50
        url = f'https://api.louisvuitton.com/api/eng-ca/catalog/filter/epy4e8?range={start}-{finish}'
    else:
        break
time(0.3)