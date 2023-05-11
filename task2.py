import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import urllib.request
from fake_useragent import UserAgent

import os

path = './projects'
# os.mkdir(path)

item_names = []
item_links = []

# URL of the page to be scraped
for p in range(121, 168):
    url = f"https://old.led7.ru/category/dizajnerskie-lyustry-i-svetilniki?page={p}"
    print('Обработка страницы ' + str(url))
    print('страница ' + str(p))

    sleep(8)
    ua = UserAgent()
    ua.random

    response = requests.get(url)


    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'lxml')

    # product_items = soup.find_all('div', class_='image')
    product_items = soup.find('ul', class_='products prd_big_preview list-style-none products_list').find_all(
        'div', class_='desc')
    print(str(len(product_items)) + ' товара(ов) на странице')


    for product in product_items:
        # item_name = product.find('img').get('alt').rstrip()
        item_name = product.find('a').text.rstrip()

        try:
            os.mkdir(path+'/'+item_name)
            print('Папка "' + path+'/'+item_name + '" создана')
        except:
            print('Ошибка создания папки "' + path+'/'+item_name+'"')

        # urllib.request.urlretrieve(product.find('img').get('src'),
        #                            path + '/' + item_name + '/' + item_name +'.jpg')

        # item_link = product.find('a').get('href')
        item_link = product.find('a').get('href')
        print('Обработка картинок товара "' + item_name + '" со страницы ' + str(item_link))
        item_names.append(item_name)
        item_links.append(item_link)

        response2 = requests.get(item_link)

        # Parse the HTML content using BeautifulSoup
        soup2 = BeautifulSoup(response2.text, 'lxml')
        try:
            product_items2 = soup2.find('div', class_='content').findAll(class_='prod_thumb')
        except:
            print("ошибка страницы ")

        for product2 in product_items2:
            sleep(0.5)
            item_name2 = product2.get('href')
            filename = os.path.basename(item_name2)
            remaining_download_tries = 30
            while remaining_download_tries > 0:
                try:
                    urllib.request.urlretrieve(item_name2,
                                               path + '/' + item_name + '/' + filename)
                    print("успешно скопирован файл: " + item_name2 + ' по пути: ' + path+'/'+item_name +'/' + filename)
                    # time.sleep(0.1)
                except:
                    print("ошибка загрузки " + item_name2 + " Попытка номер: " + str(31 - remaining_download_tries))
                    remaining_download_tries = remaining_download_tries - 1
                    sleep(1)
                    continue
                else:
                    break

print('COMPLETED!')
