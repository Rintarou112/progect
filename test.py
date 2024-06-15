import requests
import pprint
import json
url = "https://fakestoreapi.com/products"
response = requests.get(url).json()
for i in response:
    print(f'Имя: {i["title"]}')

