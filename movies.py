import sqlite3

con = sqlite3.connect('movies.db')

a = "INSERT INTO Movies(name, year, rating, genre) VALUES ('Фильм', 2018, 6.6, 'романтика')"
cur = con.cursor()

cur.execute(a)
con.commit()


cur.close()
con.close()
#Нужно ввести самостоятельно вводить данные для базы данных фильмов