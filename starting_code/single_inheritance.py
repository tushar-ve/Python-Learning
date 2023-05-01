class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("The sound made by the  animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("BArk!!!!")

d = Dog("Dog", "Doggerman")
d.make_sound()

a = Animal("Dog", "Dog")