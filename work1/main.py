import requests
from bs4 import BeautifulSoup
import os
import time
from time import sleep
import random
import json



def get_all_pages():
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ru,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'dsdportal_data=a%3A0%3A%7B%7D',
    'referer': 'https://kz24.online/companies/section52-2600.html',
    'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Linux",
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.1.575 (beta) Yowser/2.5 Safari/537.36'
}
    r = requests.get('https://kz24.online/companies/section52.html', headers=headers)
    r.encoding='utf-8'
    
    if not os.path.exists("data"):
        os.mkdir("data")
        
    #with open('data/page_1.html', 'w') as file:
        #file.write(r.text)
    with open('data/page_1.html') as file:
        src = file.read()
        
    soup = BeautifulSoup(src, 'lxml')
    pages = soup.find('table', class_='price').find_all('tr')[-1]
    pages_count = int(pages.find('td', class_='h').find_all('a')[-1].text)
    
    #for i in range(1, pages_count):
        #url = 'https://kz24.online/companies/section52' + ('-' + str(i*50)) + '.html'
        #print(url)
        #r = requests.get(url=url, headers=headers)
        #r.encoding = 'utf-8'
        
        #with open(f'data/page_{i}.html', 'w') as file:
            #file.write(r.text)
        #time.sleep(3)
    return pages_count 


def collect_data(pages_count):
    data = []
    comp_urls = []
    for page in range(1, pages_count):
        with open(f'data/page_{page}.html') as file:
            src = file.read()
            
        soup = BeautifulSoup(src, 'lxml')
        companies = soup.find('table', class_='price').find_all('tr')[1:][:-1]
        
        

        for comp in companies:
            try:
                comp_url = comp.find('a').get('href')
                comp_urls.append(comp_url)
            except:
                continue
            

        
    with open('companies_urls_list.txt', 'a') as file:
        for line in comp_urls:
            file.write(f'{line}\n')
    with open('companies_urls_list.txt') as file:
        lines = [line.strip() for line in file.readlines()]
        data_dict = []
        count = 0
        
        for line in lines:
            q = requests.get(line)
            result = q.content
            soup1 = BeautifulSoup(result, 'lxml')
            
            name = soup1.find('body').find('h1').text
            name = name.split('-')[0].split(',')[0]
            
            information = soup1.find_all('p')
            try:
                description = ''.join(information[2].text)
                description = description.split(':')[1].strip()
            except:
                description = 'Отсутствует'

            contacts = (''.join(information[4].text))
            contacts = contacts.split('\n')

            sub_email = 'E-mail'
            try:
                email = next((s for s in contacts if sub_email in s), None)
                email = email.split(':')[1].strip()
            except:
                email = 'Отсутствует'

            sub_adress = 'Адрес'
            try:
                adress = next((s for s in contacts if sub_adress in s ), None)
                adress = adress.split(':')[1].strip()
            except:
                adress = 'Отсутствует'

            sub_phone = 'Телефон'
            try:
                phone = next((s for s in contacts if sub_phone in s), None)
                phone = phone.split(':')[1].strip()
            except:
                phone = 'Отсутствует'

            sub_site = 'Сайт'
            try:
                site = information[4].find_all('a')[2].get('href')
            except:
                site = 'Отсутствует'

            sub_fax = 'Факс'
            try:
                fax = next((s for s in contacts if sub_fax in s), None)
                fax = fax.split(':')[1].strip()
            except:
                fax = 'Отсутствует'

            #sub_person = 'Контактное'
            #try:
                #person = next((s for s in contacts if sub_person in s), None)
                #person = person.split(':')[1].strip()
            #except:
                #person = 'Отсутствует'
            try:    
                categories_block = ''.join(information[3].text.strip())
                categories_info = categories_block.split('Подкатегории:')
                categories = categories_info[0].strip('Направление:').strip()
                subcategories = categories_info[1].strip()
            except:
                categories = 'Отсутствуют'
                subcategories = 'Отсутствуют'
            
            
            data = {
                'Компания': name,
                'Описание': description,
                'Адрес': adress,
                'Почта': email,
                'Телефон': phone,
                'Факс': fax,
                'Сайт': site,
                'Категории': categories,
                'Подкатегории': subcategories
            }
            count += 1
            time.sleep(random.randrange(1,3))
            print(f'{count}: {line} Выполнена')
            
            data_dict.append(data)
            with open('data.json', 'w') as json_file:
                json.dump(data_dict, json_file, indent=4, ensure_ascii=False)
            


def main():
    pages_count = get_all_pages()
    collect_data(pages_count=pages_count)
    
if __name__ == "__main__":
    main()
