import sqlite3

con = sqlite3.connect("movies.db")
cur = con.cursor()
res = cur.execute("SELECT * FROM Movies")
films = res.fetchall()



for index, name, year, rating, genre, prosmotr in films:
    print(f"Index: {index}, Name: {name}, Year: {year}, Rating: {rating}, Genre: {genre}, Prosmotr: {prosmotr}")
#for name in films:
#    print(f"Name: {name}")
a = input('Введите название: ')

flag = False
for i in films:
    if i[1] == a:
        selected_film = i
        break

selected_film = list(selected_film)
print(selected_film)
selected_film[5] += 1


b = ("UPDATE movies set prosmotr = ? where name = ?")
cur.execute(b, (selected_film, prosmotr))       
# Докончить код - обновить саму таблицу  
con.commit()

# Закрываем курсор
cur.close()

# Закрываем 
con.close()
print(selected_film)