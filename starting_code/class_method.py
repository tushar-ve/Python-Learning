class Person:
    count_instance = 0
    def __init__(self, first_name, last_name, age):
        Person.count_instance +=1
        self.first_name = first_name
        self.last_name = last_name
        self.age= age
    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} instance of Person class"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_above_18(self):
        return self.age> 18
    

p1 = Person('Tushar', 'Sharma', 4738)
p2 = Person("Harsh", "sharma", 30)
print(Person.count_instances())
    