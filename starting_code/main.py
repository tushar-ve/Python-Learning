# Video number 5 the topics are comments, Escape Sequence & print statement 
# The Comment is already known
# Escape Squences
print ("Hello Brother \n Damon!!!!!")

# In below line the code shows how we use double quotes in a print  statement separately
print ("What are you doing here \n \"Nothing\"")
#Multiple input  in the print statement "SEP" is  given separater


print("Hey What happen", 9, "thing", sep="~")


# _______V-6____Variable & Datatype________________ 
a = 0
a = "Tushar Sharma" 
# It's a interpreted language the  when we intialize a value the its would take the last value as we intialized
 

print (a)
# OUTPUT will be "Tushar Sharma ". 
# to know the datatype of a v ariable we use an  inbuilt function "_type_" 

a = 1.00  
b = True
c = "String"
d = None

print ("The type of a is ", type(a))


# _____Sequenced data: List & tuple__________
list1 =[8, 2.3, [-4, -5], ["apple", "banana"]]
print(list1)

# tuple is an ordered collection of data with the element separated by the comma & enclosed in paranthesis.
# Tuples are immutable

tuple1 = ({"helo", "how"}, {"kaise", "chlra"})
print (tuple1)

# Mapped Data Dictonary
# Dictionary contain the  key:value pair a key has a value

dict1 = {"name":"Tushar", "age":20, "vote": True}
print(dict1) 

# creating a calculator

# num1 = int(input("Enter the first number: " ))
# num2 = int(input("Enter the second number: " ))
# print("The addition of the inputs are:", num1+num2)
# print("The multiplication of the inputs are:", num1*num2)
# print("The division of the inputs are:", num1/num2)
# print("The remindar of the inputs are:", num1%num2)
# print("The square of the inputs are:", num1**num2) #this is exponential operator


#Typecasting video-09_______________
# Typecasting Divided into two categories
# Implicit Typecasting
c = 56.87
d = 8767
print(c+d)
# here python converted the integer to float automatically


# Explicit Typecasting
a ="12"
b= "11"
print(int(a)+int(b))
# here we converted the string into the integer 

# Video Lecture-11 Topic String


print('He said, "I want to eat apple"')
# triple single or double  quote will use for the multiline  string
# a = """the given task is to easy to from,
# just change the value of the given input
# """
# print(a)


name = ["tushar", "hello", "node module"]
print(name[1:3]) 


for string in name:
    print(string)


#______String Slicing________Video-12-----------
#  length of  a string can be findout through the len ......
# string slicing is basically a concept of lenth to get index value as output

len1 = len(name)
print(len1)

 
#______________String Methods in python_____________#########
#  In this there are inbuilt functions for the string to modify that....
#  Strings are immutable
# String methods work on the existing string the don't replace that string 

new_string = "Stop Syste M @@@"
print(len(new_string))
print(new_string.upper())
print(new_string.lower())
# if there is any mark at the end of the dtring we can remove that mark by using the inbuilt function rstrip

print(new_string.rstrip("@"))

#replace() is used to replace the string
print(new_string.replace("Stop", "Start")) 

# Split() is used to convert the string into the list 
print(new_string.split(" "))

# capitalize() is an a inbuilt function to capitalize the give string 
# It will convert only the  first character to the upper case

print(new_string.capitalize())

# center() is used to centralize the give string with the input space
print(len(new_string))
print(len(new_string.center(30)))


# Count() is use to check the value repeatatively in number of repeatation

print(new_string.count("@"))

# endswith() it's used to check the given string is ended with the input to know 
print(new_string.endswith("@")) 
# a variable can be overwritein python
# WE also can check the value in between
print(new_string.endswith("Syste", 4, 10))


# to find the value index number we can use find()

print(new_string.find("Sy"))

# index() is similar to the find method but it's show error when data is not found where find() shows -1
# isalnum() is provide the value a-z A-Z & 0-9
# islower() is used to know that our project consist the value in lower case or not
# isspace is the function which provide true value if there is "  " <--- this sort of space in the  string
# istitle() is a function which provide the output true if there is the 1st aphlabet capital
# swapcase() is a method which convert the lower case to uppercase 


# video number 14 Conditional statement
# conditional operator <, >, <=, >=, == 

# a = int(input("Please Enter your age: "))
# print("Your age is", a)
# if(a>19):
#     print("BRo!!!!!!! ready to drive")
# elif(a==19):
#     print(f"Don't Worry only this years you have to wait")
# else:
#     print(f"Sorry You have to wait {19-a} year more")


# Nested If Condition

a = int(input("Enter the number: "))
if (a<=12):
    if(a<6):
        print("This child is too young for 6th class")
    elif(a>6):
        print(f"This {12-a} years are pending to reach class")
else:
    print("You ar above 12 years huh!!!...")             