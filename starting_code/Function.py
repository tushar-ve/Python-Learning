# v--20

# def calculateGmean(a,b):
#     gmean = (a*b)/(a+b)
#     print(gmean)

# input1 = int(input("Enter the value 1st No:  "))
# input2 = int(input("Enter the value 2nd No:  "))
# calculateGmean(input1,input2)


#V---21
# Arguments in python 
# * makes an argument as a tuple 


# def average(*numbers):
#     sum = 0
#     for i in numbers:
#      sum = sum+i
#     print("Average is: ", sum/ len(numbers))


# average(5, 6)

# ** is used for the dictionary
def name(**name):
   print("HEllo", name["fname"], name["mname"], name["lname"])


name(mname= "Bhaishabh", lname="kha hai", fname = "kya kaam hai usse")