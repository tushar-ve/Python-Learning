def my_generator():
    for i in range(53):
        yield i


gen = my_generator()
for j in gen:
    print(j)