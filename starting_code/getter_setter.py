class Myclass:
    def __init__(self, value):
        self._value = value
    
    def show(self):
        print(f"Value is {self._value}")

# This is behave like a getter 
    @property
    def value(self):
        return self._value
    

# This is setter 
    @value.setter
    def value(self, new_value):
        self._value = new_value/10
obj = Myclass(20)
obj.value = 67
print(obj.value)

obj.show()