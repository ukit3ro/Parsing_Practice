import requests
from data import api_key

headers = {
    "user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
#response = requests.get('https://google.com')

#print(response.status_code)
#Статус ответа от сервера,
#все ответы в диапазоне [200-300] - ответ успешно получен
#От 300 до 400 - было выполнено перенаправление на другую страницу сайта
#400-500 - ошибка на стороне клиента
#500-600 - ошибка на стороне сервера

#print(response.headers)
#Служебная информация, которую передаёт наш браузер сайту

#Получение html-кода страницы:
#print(response.content) #отображение содержимого в виде байтовой строки
#print(response.text) #нормальный html-код страницы

#Параметры get-запроса
params = {
    "q": "funny cats"
}
response1 = requests.get('https://google.com', params=params)


#работа с API погоды
params1 = {
    "q": "Челябинск, " "RU",
    "appid": api_key
}
weath_resp = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params1)

#print(weath_resp.json())

#POST запросы
data = {
'custname':
'Людмила Савинкова',
'custtel':
'1233454211542',
'custemail':
'ludmilasavinkova8533@gmail.com',
'size':
'medium',
'topping':
'cheese',
'delivery':
'11:30',
'comments':
'eawrteatrgeartearg'
} #словарь с данными, которые нужно передать
response2 = requests.post('http://httpbin.org/post', headers=headers, data=data)
print(response2.text)
