# MAP()

# def cube(n):
#     return n*n*n
# l = [1,2,2,3,4,5,6]
# newl = map(cube, l)
# h = set(newl)
# print(h)


# filter

# def filter_function(a):
#     return a>4

# new2= filter(filter_function, l)
# print(list(new2))  


#Reduce

from functools import reduce

numbers = [1,2,3,4,4]

sum = reduce(lambda x, y: x+y, numbers)

print(sum)