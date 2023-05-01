

class Nmb:
    def __init__(self, num):
        self.num = num
    
    def num1(self, n):
        self.num = self.num+n

    @staticmethod
    def add(a,b):
        return a+b

    
a = Nmb(5)
print(a.num)

a.num1(6)
print(a.num)
print(Nmb.add(8,3))     