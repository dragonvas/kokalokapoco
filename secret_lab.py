print('«Секретная лаборатория»')
print('«Система управления агентами запущена.»')
print('«Для входа необходимо пройти регистрацию.»')

class Agent:
    def __init__(self, name, age, zov):
        self.name = name
        self.age = age
        self.zov = zov
    def hello(self):
        print(f'Здравствуйте, {self.zov} {self.name}')
    def show_info(self):
        print(f'Имя: {self.name}')
        print(f'Возраст: {self.age}')
        print(f'Позывной: {self.zov}')
    def secret_tasks(self):
        print('1. Убить курицу Лорд Мастер Граф Линьганигуль в чикен гане.')
        print('2. Причуть пропанвый балон.')
        print('3. Возродить Алексея Овального.')
        print('4. Установить линукс')
        print('5. Блаблеблеблю Аблебблебелю блю бле')
    def check_access(self):
        age1 = int(self.age)
        if age1 >= 14:
            return True
        else:
            print('Доступ запрёшён из-за возраста, требуется разрешение')
            return False
print("Чтобы получить доступ к лабортории надо пройти регистрацию")
agent = Agent(input('Имя:'),int(input('Возраст:')),input('Позывной:'))
print('Регистрация успешна!')
if agent.check_access():
    agent.hello()
while True:
    print('1. Информацня')
    print('2. Задания')
    choose=int(input('Что вы хотите сделать?'))
    if choose == 1:
        agent.show_info()
    elif choose == 2:
        agent.secret_tasks()
    else:
        print('Нет такого действия')
