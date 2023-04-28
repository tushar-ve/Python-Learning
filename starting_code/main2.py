#______________DAY-2______________
# ---- 10MIN for Sla Form Completed
# strftime() is function which provides the time in hr, min, sec 

import time
# timestamp = (time.strftime('%H:%M:%S'))
# print(timestamp)
# if(timestamp>12):
#     print("Good Morning Sir")
# else:
#     print("Nothing") 
# input1= int(input(time('%H'))) 
# # input2= (input(time.strftime('%M'))) 

# # input3= int(input(time.strftime('%S'))) 
# print(input1)

# input2= int(time.strftime('%M')) 
# print(input2)

#____________Match__CAse___ V-16
#  The match case statement is basically the switch statement of the python 
# Let's make a program 
# x = int(input("Enter Your age")) 
# match x:
#     case 12:
#         print("You are not allowed for car race matches")
#     case 11:
#         print("Something more")

# __________Video-17 Loops__________________

# # WAP to print number in the given secanior



# input1 = int(input("Enter the value1 : "))
# input2 = int(input("Enter the value2 : "))

# for i in range(input1, input2+1):
#     if(input1<input2):
#         print(i)
#     else:
#         print("1st value is greater than the last please recheck") 


# Print a list in for loop with it's sperated words as well

# colors = ["Blue", "Eye", "Hypnotise", "Teri", "Kardi"]
# for color in colors:
    
#     for i in color:
#         print(i)
    
#     print(color)
 
#  #Print the table  of any given number
# number1 = int(input("Enter the value1 : "))
# for i in range(number1, number1*11, number1):
#     print(i)


#_____________While___Loop___ V-18__________
# i = int(input("PLease Enter the value: "))
# while(99>i>38):
#     print("The given number is good to go ")
      
# if(i>99):
#         print(f"You need to decrease the number by {i-99}")
# elif(i<38):
#         print(f"You have to Increase the number by: {38-i}") 

 
#_____________Video-19______________Break & Continue statement

# Break is used to make a break in statement

for i in range(14):
    if(i==12):
        break
    print("5  X ", i+1, "=", 5 * (i+1))
print("loop terminated")
