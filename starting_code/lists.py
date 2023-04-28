marks = [22, 28, 24]
# print(type(marks))

# in keyword is used to check the item is in the list or not 
# if "True" in marks:
    # print("yes it's there")
    #  to print the element all in the list we can use the concep of [:]
    # but easy is to print list name print()
    # print(marks)
    # print(marks[:])
    # print(marks[1:4:2])


    # list comprehensive 
# lst = [i*i for i in range(12) if i%2 ==0]
# print(lst)
#  Video --23--________________

#  append add the item in the end of the list
# marks.append(90)
# print(marks)
# Output ===== [22, 23, 24, 'True', True, 90]
# print(marks)

# sort function is used to sort the list 

# marks.sort()
# print(marks)



# reverse is use to reversed the list
# marks.reverse()
# print(marks)

# count is use to count the repeatative items number
# print(marks.count(23))

# We can make the copy of the given list
# m = marks.copy()
# print(m)

#  We use insert to insert  on the particular index of  the list 

# marks.insert(2,8988)
# print(marks)


k = ["john", "jerry", "jj"]

marks.extend (marks)
print(marks) 


i = [k.append(input("Enter new string")) for i in range(3)]
print(k)

