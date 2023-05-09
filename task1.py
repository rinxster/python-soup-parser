
import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

item_names = []
item_links = []

# URL of the page to be scraped
for p in range(1, 168):
    url = f"https://old.led7.ru/category/dizajnerskie-lyustry-i-svetilniki?page={p}"
    print(url)
    sleep(7)
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'lxml')

    # product_items = soup.find_all('div', class_='desc')
    product_items = soup.find('ul', class_='products prd_big_preview list-style-none products_list').find_all(
        'div', class_='desc')

    print(len(product_items))

    for product in product_items:
        remaining_download_tries = 30

        while remaining_download_tries > 0:
            try:
                print(product.find('a').text.rstrip())
                print(product.find('a').get('href'))

                item_name = product.find('a').text.rstrip()
                item_link = product.find('a').get('href')
                item_names.append(item_name)
                item_links.append(item_link)

            except:
                print("error downloading " + item_name + " on trial no: " + str(31 - remaining_download_tries))
                remaining_download_tries = remaining_download_tries - 1
                sleep(1)
                continue
            else:
                break
    # save data into excel file
    data = {'Item Name': item_names, 'Link': item_links}
    df = pd.DataFrame(data)
    df.to_excel('output.xlsx', index=False)
print('COMPLETED!')
