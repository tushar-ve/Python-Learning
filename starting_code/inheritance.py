class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee : {self.id} is {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")

class Student(Employee):
    def showLanguage(self):
        print("The default language is Python")

e = Employee("Tushar Sharma", 11690 )
e1 = Programmer("Sharma Tushar", 11456)
e2 = Programmer("Rohan", 11456)
e2.showDetails()
e.showDetails()