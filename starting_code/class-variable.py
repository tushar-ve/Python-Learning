# Class variable declaration

# class Cirlce:
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius
#     def cal_curcumference(self):
#         return 2*Cirlce.pi*self.radius

# c1= Cirlce(6)
# print(c1.cal_curcumference())


# class Laptop:
#     discount_app = 20 #here we R creating class variable
#     def __init__(self, brand_name, model_name, price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = price
#     def Discount(self):
#         off_price = (Laptop.discount_app/100)*self.price
#         return (self.price - off_price)


# lap1 = Laptop("HP", "tukm909", 56789)
# lap2 = Laptop("Dell", "kjkw09ksl", 89738)

# # printing an a value of the given objects
# print(lap2.__dict__)

# # print(lap1.Discount())

# if we have to run discount individual for the other laptop

class Laptop:
    discount_app = 20 #here we R creating class variable
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
    def Discount(self):
        off_price = (self.discount_app/100)*self.price
        return (self.price - off_price)


lap1 = Laptop("HP", "tukm909", 56789)
lap2 = Laptop("Dell", "kjkw09ksl", 89738)

lap2.discount_app = 50
print(lap2.__dict__)
print(lap2.Discount())

