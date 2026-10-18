
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
        age = {self.age}
        age = int(age)
        if age >= 14:
            pass
        else:
            pass

print("Чтобы получить доступ к лабортории надо пройти регистрацию")
agent = Agent(input('Имя:'),int(input('Возраст:')),input('Позывной:'))
print('Регистрация успешна!')
agent.hello()
agent.show_info()
agent.secret_tasks()