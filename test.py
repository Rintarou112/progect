import requests
import pprint
import json

url = "https://fakestoreapi.com/products/categories"
response = requests.get(url).json()

print('Список категорий товаров: ')
print(', '.join(response))

a = input('Введите категорию товара: ')

flag = False
for i in response:
    if i == a:
         url_a = f"https://fakestoreapi.com/products/category/{a}?sort=desc"
         response_a = requests.get(url_a).json()
         print('Товары категории:', a)
         for i in response_a:
            print(f'Название: {i['title']}\nКатегория: {i['category']} \nЦена: ${i['price']} \nОписание: {i['description']}\n')
         flag = True
if not flag:
    print('Нет такой категории товара')    
