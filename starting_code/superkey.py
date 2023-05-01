class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id =id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

e1 = Employee("Harry", 3847)
e2 = Programmer("Tushar", "36743", "Python")
print(e2.id)
