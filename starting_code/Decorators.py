# @ use for the decorator |||| also known AS SYNTATIC SUGAR

from functools import wraps



def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        """This wrapper Function"""
        print('This function is awesome')
        return any_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def func1(c):
    print(f'this is function 1 {c}')

func1(22332211)

@decorator_function
def func2(a,b):
    """This is add function"""
    return a+b


print(func2.__doc__)
print(func2.__name__)
print(func2(5,7))