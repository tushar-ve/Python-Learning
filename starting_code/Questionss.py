import os 
f = open("file.txt", 'r')
data = f.read()
for i in range(data):
    data.readline(i)
print(data)



