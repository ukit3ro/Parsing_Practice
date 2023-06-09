import requests
from requests import Session
import json
from bs4 import BeautifulSoup
import time
import random

# мимикрируем под ajax-запросы, получаем из json словаря информацию
# url = 'https://scrapingclub.com/exercise/ajaxdetail/'

# response = requests.get(url).json()

# print(response['title'])
# print(response['price'])
# print(response['description'])


# работа с бесконечной прокруткой
base_url = 'https://scrapingclub.com/exercise/list_infinite_scroll/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}


def main(base_url):
    s = Session()
    s.headers.update(headers)
    pagination = 0
    count = 1
    while True:
        if count > 1:
            url = base_url + '?page=' + str(count)
        else:
            url = base_url

        resp = s.get(url)
        soup = BeautifulSoup(resp.text, 'lxml')

        if count == 1:
            pagination = int(soup.find('ul', class_='pagination invisible').find_all('li', class_='page-item')[-2].text)

        cards = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
        for card in cards:
            name = card.find('h4', class_='card-title').text
            price = card.find('h5').text
            print(name, price)
        print(count)
        time.sleep(random.choice([1,2,3]))

        if count > pagination:
            break
        count += 1

main(base_url)
