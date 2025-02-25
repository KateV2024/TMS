import sqlite3


# Подключаемся к базе данных (создаст файл, если его нет)
conn = sqlite3.connect("university.db")
cursor = conn.cursor()
cursor.execute("SELECT * from users;")

# Получаем результат

db_version = cursor.fetchall()
print(f"Всем юзеры {db_version}")

# Закрываем соединение
conn.close()
