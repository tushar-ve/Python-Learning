#  Access modifier are the property where the variable or object are accessed in ways:-
# 1. Private _Access_Modifier 
# 2. Public Access
# 3. Protected 

class Employee:
    def __init__(self):
        self.name = "HArry1"
        self.__age = 14 # private property of object

a = Employee()
print(a.name) #Here we accessing the part of the Employee class

print(a._Employee__age) # aaaaccessing that private variable



# Let's take an example of the 