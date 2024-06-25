import sqlite3

# Устанавливаем соединение с базой данных "movies.db"
con = sqlite3.connect('movies.db')

# Создаем курсор для выполнения запросов
cur = con.cursor()

name = input('Имя: ')
year = int(input('Год: '))
rating = float(input('Рейтинг: '))
genre = input('Жанр: ')

# Строка SQL-запроса для добавления новой записи в таблицу "Movies" и сразу выполняем его
cur.execute("INSERT INTO Movies(name, year, rating, genre) VALUES (?, ?, ?, ?)", (name, year, rating, genre))
# cur.execute - выполняет SQL-запрос

# Сохраняем изменения в базе данных
con.commit()

# Закрываем курсор
cur.close()

# Закрываем 
con.close()
