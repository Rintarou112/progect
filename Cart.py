import requests
import json

url = "https://fakestoreapi.com/carts"
response = requests.get(url).json()

print('Список категорию товаров: ')
print(response)



   