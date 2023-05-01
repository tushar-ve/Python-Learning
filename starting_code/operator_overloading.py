class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    def __str__(self) :
        return f"{self.i}i + {self.j}j + {self.k}k"
    def __add__(self,x):
        return Vector(self.i + x.i, self.k+x.k , self.j + x.j)
    
v1 = Vector(3,4,6)
print(v1)

v2 = Vector(5,6,7)
print(v2)

print(v1+v2)