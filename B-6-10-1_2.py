class Restangle:
    def __init__(self, x, y, width, hight):
        self.x = x
        self.y = y
        self.w = width
        self.h = hight
    def print_exemplar(self):
        R = "Restangle (" + str(self.x) + "," + str(self.y) + "," + str(self.w) + "," + str(self.h) + ")"
        return R
    def restangle_area(self):
        return self.w * self.h
r1 = Restangle(1,2,3,4)
r2 = Restangle(5,6,7,8)
r3 = Restangle(9,8,7,6)
print(r1.print_exemplar())
print(r1.restangle_area())
print(r2.print_exemplar())
print(r2.restangle_area())
print(r3.print_exemplar())
print(r3.restangle_area())