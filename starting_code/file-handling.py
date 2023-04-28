# f = open('file.txt', 'r')
# # print(f)
# text = f.read()
# print(text)
# f.close()


# Write a file 

# f = open("file.txt", 'a')
# f.write("this is something different")
# f.close()

# Using with for write a file 
  
# with open('file.txt', 'a') as f:
#     f.write("Hey I am inside with ")


# readline() use to access the data line by line 
# f = open("file.txt", 'r')
# i = 0
# while True:
#     i= i+1
#     line = f.readline()
#     if not line:
#         break 
#     print(line)



# writelines() 
# f = open('file.txt', 'w')
# lines = ['line \n', 'line\n', 'line line line bss bhut hua \n']
# f.writelines(lines)
# f.close()
# f = open('file.txt', 'r')
# text = f.read()
# print(text)


# seek() is to start when value from the skipped bytes 
# tell() provides the value inthe where we seeked from 


with open('file.txt', 'r') as f:
    print(type(f))

    f.seek(10)
    print(f.tell())

    data = f.read(5)
    print(data)
  

