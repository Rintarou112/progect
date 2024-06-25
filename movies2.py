import sqlite3

# Устанавливаем соединение с базой данных "movies.db"
con = sqlite3.connect('movies.db')

d = ['','','','']
z = ['name', 'year', 'rating', 'genre']
for i in range(0,4):
    d[i] = input(f'Введите {z[i]}')
# Создаем курсор для выполнения запросов


# Строка SQL-запроса для добавления новой записи в таблицу "Movies" и сразу выполняем его
cur.execute("INSERT INTO Movies(name, year, rating, genre) VALUES (?, ?, ?, ?)", ('{d[0]}', '{d[1]}', '{d[2]}', '{d[3]}'))
# cur.execute - выполняет SQL-запрос
cur = con.cursor()
# Сохраняем изменения в базе данных
con.commit()

# Закрываем курсор
cur.close()

# Закрываем 
con.close()
