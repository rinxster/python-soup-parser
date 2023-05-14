import requests
import random
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import urllib.request

import os

item_names = []
item_links = []

# URL of the page to be scraped
for p in range(1, 168):
    url = f"https://old.led7.ru/category/dizajnerskie-lyustry-i-svetilniki?page={p}"
    print('Обработка страницы ' + str(url))
    print('страница ' + str(p))

    sleep(random.randint(0,9))

    response = requests.get(url)


    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'lxml')

    remaining_download_tries = 300
    while remaining_download_tries > 0:
        try:
            product_items = soup.find('ul', class_='products prd_big_preview list-style-none products_list').find_all(
                'div', class_='desc')
            print(str(len(product_items)) + ' товара(ов) на странице')

        except:
            print("ошибка загрузки product_items. Попытка номер: " + str(301 - remaining_download_tries))
            remaining_download_tries = remaining_download_tries - 1
            sleep(random.randint(0,5))
            continue
        else:
            break


    for product in product_items:
        remaining_download_tries2 = 300
        while remaining_download_tries2 > 0:
            try:
                # item_name = product.find('a').text.rstrip().replace(":", "").replace("/", "")
                item_name = product.find('a').text.rstrip()

                item_link = product.find('a').get('href')
                print('Товар: "' + item_name + '" страница: ' + str(item_link))
                item_names.append(item_name)
                item_links.append(item_link)
            except:
                print("ошибка загрузки " + item_name + " Попытка номер: " + str(301 - remaining_download_tries2))
                remaining_download_tries2 = remaining_download_tries2 - 1
                sleep(random.randint(0, 5))
                continue
            else:
                break

    data = {'Item Name': item_names, 'Link': item_links}
    df = pd.DataFrame(data)
    df.to_excel('output.xlsx', index=False)
print('COMPLETED!')
