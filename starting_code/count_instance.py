# Exercise of the instance variable

class Person:
    count_instance = 0

    def __init__(self, student_id, Name, Marks):
        Person.count_instance += 1
        self.student_id = student_id
        self.Name = Name
        self.Marks = Marks



p1 = Person(12345, "Rohan", 89)

p2 = Person(98776, "Nitish", 77)
print(Person.count_instance)