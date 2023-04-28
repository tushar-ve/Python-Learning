# class Person:
#     def __init__(self, first_name, last_name, age):
#         # instance variable creation 
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

# p1 = Person('Tushar', 'sharma', 21)
# p2  = Person('Maddy', 'Sharma', 13)

# print(p1.first_name)


# class Laptop:
#     def __init__(self, brand_name, model_name, price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = price

# lap1=Laptop("HP", "tukm909", 56789)
# lap2 = Laptop("Dell", "kjkw09ksl", 89738)

# print(lap1.price)

# How to define method & self we declare 


# class Person:
#     def __init__(self, first_name, last_name, age):
#         # instance variable creation 
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
    
#     def is_above_18(self):
#         return self.age>18

# p1 = Person('Tushar', 'sharma', 21)
# p2  = Person('Maddy', 'Sharma', 13)

# print(p1.is_above_18())
# print(p2.is_above_18())


class Laptop:
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
    def Discount(self, less):
        off_price = (less/100)*self.price
        return (self.price - off_price)


lap1 = Laptop("HP", "tukm909", 56789)
lap2 = Laptop("Dell", "kjkw09ksl", 89738)

print(lap1.Discount(20))
