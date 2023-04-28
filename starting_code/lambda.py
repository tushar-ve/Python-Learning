def double(x):
    return x*2

double = lambda X:X*2
print(double(9))

def app(fx,  value):
    return 6 + fx(value)


print(app(double, 3))

