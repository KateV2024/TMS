import sqlite3


# Подключаемся к SQLite (или создаем новый файл БД)
conn = sqlite3.connect("university.db")
cursor = conn.cursor()

# Создаёт тестового пользователя
cursor.execute("""
INSERT INTO users (name, email, age, country) VALUES (?, ?, ?, ?)
""", ("Kate", "kate@example.com", 32, "Poland"))

# Доказывает, что пользователь появился в БД
cursor.execute("SELECT * from users where name='Kate';")

# Получаем результат
db_version = cursor.fetchone()
print(f"Наш добавленный юзер {db_version}")

# Удаление тестоваго юзера
cursor.execute("DELETE FROM users WHERE name='Kate'")
conn.commit()

cursor.execute("SELECT * FROM users WHERE name='Kate';")
deleted_user = cursor.fetchone()

if deleted_user:
    print(f"Юзер остался в базе: {deleted_user}")
else:
    print("Юзер успешно удалён.")

# Закрываем соединение
conn.close()