class Guests:
    def __init__(self, name, sity, status):
        self.n = name
        self.s = sity
        self.status = status
    def print_guest(self):
        G = str(self.n) + ", " + str(self.s) + ', статус "' + str(self.status) + '"'
        return G

class Bad_Guests (Guests):
    comment = "посадить в угол и не кормить!!!"

G1 = Guests("Иванов Иван","г.Москва","Наставник")
G2 = Guests("Петров Василий","г.Москва","Ментор")
G3 = Bad_Guests("Тот-Кто-Придумал-Эти-Задачи","д.Гадюкино","Садист")
print(G1.print_guest())
print(G2.print_guest())
print(G3.print_guest() + " - " + G3.comment)
