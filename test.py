import requests
import pprint
import json

url = "https://fakestoreapi.com/products/categories"
response = requests.get(url).json()
print(response)
print('Список категорию товаров: ')
for i in response:
    print(i)

def tovar(a):
    for i in response:
        if i == a:
            print('Вы выбрали:',a.title())
        


a = input('Введите категорию товара: ')
b = tovar(a)




