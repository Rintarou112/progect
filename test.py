import requests
import pprint
import json

url = "https://fakestoreapi.com/products/categories"
response = requests.get(url).json()
print(response)
print('Список категорию товаров: ')
for i in response:
    print(i.title())


def tovar(a):
    flag = False
    for i in response:
        if i == a:
            print('Вы выбрали:',a.title())
            flag = True
    if not flag:
        print('Нет такой категории товара')    


a = input('Введите категорию товара: ')
b = tovar(a)




