import requests
import pprint
import json

url = "https://fakestoreapi.com/products/categories"
response = requests.get(url).json()

print('Список категорию товаров: ')
print(', '.join(response))

a = input('Введите категорию товара: ')

flag = False
for i in response:
    if i == a:
         print('Вы выбрали:',a.title())
         flag = True
if not flag:
    print('Нет такой категории товара')    








