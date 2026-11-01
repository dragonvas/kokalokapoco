import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        age INTEGER NOT NULL
    )
""")
conn.commit()

try:
    cursor.execute(
        "INSERT INTO users (name) VALUES (?)",
        ("kykra",)
    )
    conn.commit()
    cursor.execute(
        "SELECT id name age FROM users WHERE name = ?",
        ("kykra",)
    )
    conn.commit()

    users = cursor.fetchone()

    if users != None:
        print('Пользователь найден!')
    else:
        print('Пользователь не найден.')
except sqlite3.IntegrityError:
    print('Пользователь уже существует')

cursor.execute("SELECT id, name, age FROM users")
user_all=cursor.fetchall()

if user_all:
    print('Список пользователей')
    for user in user_all:
        print(f"ID: {user[0]}, Имя: {user[1]}, Возраст: {user[2]}")
else:
    print('Нет пользователей')

new_age=int(input('Введите новый возраст'))
user_id=int(input('Введите айди игрока'))
cursor.execute(
    "UPDATE users SET age = ? WHERE id = ?",
    (new_age, user_id)
)
conn.commit()

user_id=int(input('Введите айди пользователя, которого надо удалть'))
cursor.execute(
    "DELETE FROM users WHERE id = ?",
    (user_id,)
)
conn.commit()

cursor.execute("SELECT id, name, age FROM users")
user_all=cursor.fetchall()

if user_all:
    print('Список пользователей')
    for user in user_all:
        print(f"ID: {user[0]}, Имя: {user[1]}, Возраст: {user[2]}")
else:
    print('Нет пользователей')
