import time
import os
#import msvcrt
import random
import sqlite3
connection=sqlite3.connect("database.db")
cursor=connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
)
""")
connection.commit()

time.sleep(0.01)
vibor=-1
dyblon=10
name=''
def clear():
    os.system("clr" if os.name == "nt" else "clear")
#def enter():
    #key = msvcrt.getch()
    #if key in (b'\r',b'\n'):
        #return True
    #else:
        #return False
def menu():
    global vibor, name
    print('Я робот консольный. Сделан Бисей')
    print()
    print('Выберите что хотите сделать')
    print('[1] Знакомство')
    print('[2] Казино')
    print('[0] Выход')
    print()
    vibor=input()
    if vibor == "":
        clear()
    else:
        vibor = int(vibor)
def znakomstvo():
    global name
    print('Как вас звать?????????????????????????????????????????')
    name=input()
    cursor.execute(
    "SELECT name FROM users WHERE name=?",
    (name,)
    )
    user=cursor.fetchone()
    if user:
        print(f"Привет, {name}")
    else:
        print('Имя не найдено, вношу в базу данных')
        cursor.execute(
        "INSERT INTO USERS (name) VALUES (?)",
        (name,)
        )
def musor_drop():
    global dyblon
    print('Добро пожаловать в казино!!!!')
    stavka=-1
    while True:
        if dyblon <= 0:
            print('Недастаточно средств')
            break
        print('Ваш балланс',dyblon,'дублонов')
        stavka=int(input('Ваша ставка (в дублонах)(поставте 0 для выхода):'))
        if stavka > dyblon:
            print('Ставка привышает баланс')
        elif stavka < 0:
            print('Ставка слишком низкая')
        elif stavka == 0:
            break
        else:
            dyblon -= stavka
            stavka = stavka*random.randint(a=0, b=2)
            dyblon += stavka
def zakritye():
    print('ПРОГРАММА ЗАВЁРШИТСЯ ЧЕРЕЗ')
    print('5')
    time.sleep(1)
    print('4')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    exit()

while True:
    menu()
    if vibor == 1:
        znakomstvo()
    elif vibor == 2:
        musor_drop()
    elif vibor == 0:
        zakritye()