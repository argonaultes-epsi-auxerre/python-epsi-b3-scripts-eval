import sqlite3
import random


def create_table(connection):
    sql = "CREATE TABLE words(id integer primary key, word text not null, created_at date default current_date)"
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()


def truncate_table(connection):
    sql = "DELETE FROM words"
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()


def insert_data(connection, id, word):
    sql = "INSERT INTO words (id, word) VALUES (?, ?)"
    cursor = connection.cursor()
    cursor.execute(sql, (id, word))
    cursor.close()


def random_word():
    words = [
        "stubborn",
        "diplomat",
        "organize",
        "infinite",
        "flexible",
        "consider",
    ]
    return random.choice(words)


connection = sqlite3.connect("./words.db")
try:
    create_table(connection)
except sqlite3.OperationalError:
    print("Ignore existing table")
truncate_table(connection)
# insérer 10 lignes en table avec l'id allant de 1 à 10
for i in range(1, 10, 2):
    word = random_word()
    insert_data(connection, i, word)
connection.commit()

sql = "SELECT word FROM words"
cursor = connection.cursor()
res = cursor.execute(sql)
list_of_records = res.fetchall()
list_of_words = [word for word, in list_of_records]
print(list_of_records)
print(list_of_words)
cursor.close()
connection.close()
