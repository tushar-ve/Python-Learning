#can we drive the more than one class from a base class ?/
#multilevel inheritance 

# method of ovrerriding 
# isinstance() , issubclass() 


class Phone :
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)

    def full_name(self):
        return f"{self.brand} {self.model_name}"
    

    def make_a_call(self, number):
        return f"calling {number}"
    

class SmartPhones(Phone):
    def __init__(self, brand, price, model_name, ram, internal_memory, rear_camera):
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera
    def full_name(self):
        return f"{self.brand} {self.model_name} and the price is {self._price}"
class SmartPhones2(Phone):
    def __init__(self, brand, price, model_name, ram, internal_memory, rear_camera):
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

class Flapship(SmartPhones):
    def __init__(self, brand, price, model_name, ram, internal_memory, rear_camera, front_camera):
        super().__init__(brand, price, model_name, ram, internal_memory, rear_camera)
        self.front_camera = front_camera


a = Flapship("Xiamoi",  34567,"Note10", '6Gb', '64GB', '20MP','5MP')

print(a.full_name())