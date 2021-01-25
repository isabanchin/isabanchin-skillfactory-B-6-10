class Client:
    def __init__(self,name,balance):
        self.n = name
        self.b = balance

c1 = Client(name = "Иван Петров", balance = 50)

print("Клиент \"" + c1.n + "\". Баланс: " + str(c1.b) + " руб.")