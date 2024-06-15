import requests
import pprint
import json

url = "https://fakestoreapi.com/products/categories"
response = requests.get(url).json()
print(response)




