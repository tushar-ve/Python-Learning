# class Person:
#     count_instance = 0
#     def __init__(self, first_name, last_name, age):
#         Person.count_instance +=1
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age= age
#     @classmethod
#     def count_instances(cls):
#         return f"You have created {cls.count_instance} instance of Person class"
    
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
    
#     def is_above_18(self):
#         return self.age> 18
    

# p1 = Person('Tushar', 'Sharma', 4738)
# p2 = Person("Harsh", "sharma", 30)
# print(Person.count_instances())


# string = "Hello-1234"
# e = (string.split("-"))
# print(e)

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

# e2 = Employee(e[0], e[1])
# print(e2.name)
# print(e2.salary)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))
    
string = "Rohan-09354"
e2 = Employee.fromstr(string)
print(e2.name)
print(e2.salary)
# help(Employee)

print(dir(e2))
print(e2.__dict__)


