import sqlite3

conn = sqlite3.connect("deltabase.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    )
""")
conn.commit()

try:
    cursor.execute(
        "INSERT INTO user (name) VALUES (?)",
        ("kykra",)
    )
    conn.commit()
    cursor.execute(
        "SELECT id name FROM user WHERE name = ?",
        ("kykra",)
    )
    conn.commit()

    user = cursor.fetchone()

    if user != None:
        print('Пользователь найден!')
    else:
        print('Пользователь не найден.')
except sqlite3.IntegrityError:
    print('Пользователь уже существует')

cursor.execute("SELECT id, name FROM user")
user_all=cursor.fetchall()

if user_all:
    print('Список пользователей')
    for user in user_all:
        print(f"ID: {user[0]}, Имя: {user[1]}")
else:
    print('Нет пользователей')