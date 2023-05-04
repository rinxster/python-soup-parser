# built based on https://www.youtube.com/watch?v=vtizH9w0V7c

import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

item_names = []
item_links = []

# URL of the page to be scraped
for p in range(1, 168):
    url = f"https://old.led7.ru/category/dizajnerskie-lyustry-i-svetilniki?page={p}"
    print(url1)
    sleep(10)

    response = requests.get(url1)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'lxml')

    product_items = soup.find_all('div', class_='image')

    print(len(product_items))

    for product in product_items:
        item_name = product.find('img').get('alt')
        item_link = product.find('a').get('href')
        item_names.append(item_name)
        item_links.append(item_link)

    # save data into excel file
    data = {'Item Name': item_names, 'Link': item_links}
    df = pd.DataFrame(data)
    df.to_excel('output.xlsx', index=False)
print('COMPLETED!')



