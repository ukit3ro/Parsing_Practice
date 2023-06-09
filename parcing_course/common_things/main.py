import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}


def get_url():
    for count in range(1, 8):

        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'

        response = requests.get(url=url, headers=headers)
        #print(response.status_code)

        soup = BeautifulSoup(response.text, 'lxml')
        #print(soup)

        data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
        for prod in data:
            card_link = 'https://scrapingclub.com' + prod.find('a').get('href')
            yield card_link


def array():
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)
        sleep(3)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find('div', class_='card mt-4 my-4')

        name = data.find('h3', class_='card-title').text
        price = data.find('h4').text
        desc = data.find('p', class_='card-text').text
        img_url = 'https://scrapingclub.com'+data.find('img', class_='card-img-top img-fluid').get('src')
        yield name, price, desc, img_url


