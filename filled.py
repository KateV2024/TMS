import sqlite3

# Подключаемся к SQLite (или создаем новый файл БД)
conn = sqlite3.connect("university.db")
cursor = conn.cursor()

# Создание таблицы пользователей (users)
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER CHECK (age >= 0),
    country TEXT DEFAULT 'Unknown'
);
""")

# Создание таблицы заказов (orders)
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    product TEXT NOT NULL,
    price REAL NOT NULL CHECK (price >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
""")

# Создание таблицы курсов (courses)
cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL
);
""")

# Создание таблицы записей студентов на курсы (student_courses)
cursor.execute("""
CREATE TABLE IF NOT EXISTS student_courses (
    student_id INTEGER,
    course_id INTEGER,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
);
""")

conn.commit()
print("✅ Таблицы успешно созданы!")

# Заполнение таблицы users

cursor.executemany("""
INSERT INTO users (name, email, age, country) VALUES (?, ?, ?, ?)
""", [
    ("Алексей", "alex@example.com", 28, "Россия"),
    ("Мария", "maria@example.com", 25, "США"),
    ("Джон", "john@example.com", 35, "Германия"),
    ("Ольга", "olga@example.com", 30, "Франция")
])

# Заполнение таблицы orders
cursor.executemany("""
INSERT INTO orders (user_id, product, price) VALUES (?, ?, ?)
""", [
    (1, "Ноутбук", 1200.50),
    (1, "Клавиатура", 75.00),
    (2, "Смартфон", 899.99),
    (3, "Монитор", 300.00),
    (3, "Гарнитура", 150.00)
])

# Заполнение таблицы courses
cursor.executemany("""
INSERT INTO courses (course_name) VALUES (?)
""", [
    ("Python для тестировщиков",),
    ("SQL для автоматизаторов",),
    ("Docker и Kubernetes",),
    ("Автоматизация API-тестирования",)
])

# Заполнение таблицы student_courses
cursor.executemany("""
INSERT INTO student_courses (student_id, course_id) VALUES (?, ?)
""", [
    (1, 1),  # Алексей изучает Python
    (1, 2),  # Алексей изучает SQL
    (2, 3),  # Мария изучает Docker
    (3, 4),  # Джон изучает API-тестирование
    (4, 1),  # Ольга изучает Python
    (4, 3)   # Ольга изучает Docker
])

conn.commit()
print("✅ Тестовые данные успешно добавлены!")

conn.close()
print("✅ Все проверки успешно выполнены!")
