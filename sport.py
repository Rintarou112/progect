import sqlite3

con = sqlite3.connect('athletes.db')
cur = con.cursor()
res = cur.execute("SELECT * FROM athletes")
sports = res.fetchall()


print('Имя спортсмена:' )
for i in sports:
    print(i[1], end=', ') 
print("\n" )

name_sport = input('Введите имя спортсмена: ')

flag = False
for i in sports:
    if i[1] == name_sport:
        name_sports = i      
        print(f'Имя: {name_sports[1]}, Пол: {name_sports[2]}, Возраст: {name_sports[3]}, Страна: {name_sports[4]}, Вид спорта: {name_sports[5]}')
        flag = True
        break
if not flag:
    print('Нет информации')

new_name = input('Добавить нового пользователя?: ')

if new_name.lower() == 'да':
    name = input('Введите имя спортсмена: ')
    gender = input('Введите пол: ')
    age = input('Введите возраст: ')
    country = input('Введите страну: ')
    sport = input('Введите вид спорта: ')

    cur.execute("INSERT INTO athletes(name, gender, age, country, sport) VALUES (?, ?, ?, ?, ?)", (name, gender, age, country, sport))
    con.commit()

    print()

else:
    print('Продолжаем')




cur.close()
con.close()