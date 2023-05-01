# 1.Write a program that takes two numbers as input from the user and displays their sum.

# hello
# 2.Write a program that takes a string as input from the user and prints out the number of vowels in the string 

# l1 = input("Enter your string: ")

# l2 =["a", "i","o","e","u","A","I","E","O","U"]
# count = 0
# for i in l1:
#     if i in l2:
#         count = count+1
# print(count)



# 7.Write a Python program that takes a list of integers and returns a new list containing only the even integers from the original list.

# l = [2, 3, 4, 6,5]
# lst =[i for i in l if i%2==0]
# print(lst)
  
# 3.Write a program that takes a list of numbers as input and returns the largest number in the list.

# ls = []
# for l in range(5):
#     l = int(input("Enter the number"))
#     ls.append(l)
#     print(ls)

# j = sorted(ls)
# print(j[-1])



# Write a program that takes a list of strings as input and returns the longest string in the list.   string_list=['apple', 'banana', 'cherry', 'dragonfruit']
# string_list=['apple', 'banana', 'dragonfruit', 'cherry']

# string_list.sort()
# print(string_list[-1])


# 5.Write a program that takes a string as input from the user and prints out the string in reverse order.  
# l = input("Enter your String: ")
# print(l[::-1])


# 9.Write a Python program that takes a list of numbers and returns a new list containing the squares of the even numbers in the original list.
# l = [2, 3, 4, 6,5]
# lst =[i*i for i in l if i%2==0]
# print(lst)

# text = open("file.txt", "r")

# d = dict()

# for line in text:

#    line = line.strip()
#    words = line.split(" ")

#    for word in words:

#       if word in d:

#          d[word] = d[word] + 1

#       else:
#         d[word] = 1

# for key in list(d.keys()):
#    print(key, ":", d[key])


# ip_str=input("Enter a String: ")

# ip_str.casefold() #csefold() make the string in the lower case

# count={x:sum([1 for char in ip_str if char ==x])for x in 'aeiou'}
# print(count)