import requests
import json

url = 'https://fakestoreapi.com/products'
response = requests.get(url).json()
#pprint.pprint(response)

d = json.dumps(response)

print(d[1])


