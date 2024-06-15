import requests


url = 'https://fakestoreapi.com/products'
response = requests.get(url).json()
#pprint.pprint(response)

d = json.dumps(response, indent=4)

data = input('Какой')
response = requests.get(url).json()
flag = False
for i in response:
    if i ['name']['lastname'] == data:
       print(f'Имя: {i["name"]["firstname"]}, Фамилия: {i["name"]["lastname"]} ')
       print(f'Телефон: {i["phone"]}, Email: {i["email"]}')
       flag = True
if not flag:
    print('Нет')


