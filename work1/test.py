import requests
from bs4 import BeautifulSoup

q = requests.get('https://autoboom.kz24.online/')
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

sub_person = 'Контактное'
try:
    person = next((s for s in contacts if sub_person in s), None)
    person = person.split(':')[1].strip()
except:
    person = 'Отсутствует'
  
try:    
    categories_block = ''.join(information[3].text.strip())
    categories_info = categories_block.split('Подкатегории:')
    categories = categories_info[0].strip('Направление:').strip()
    subcategories = categories_info[1].strip()
except:
    categories = 'Отсутствуют'
    subcategories = 'Отсутствуют'

    

    
print(f'Компания {name}\nПо адресу {adress}')
print(f'Описание: {description}')
print(f'Контакты:\nПочта: {email}\nТелефон: {phone}\nСайт: {site}\nФакс: {fax}\nПредставитель: {person}')
print(f'Категории: {categories}, Подкатегории: {subcategories}')

