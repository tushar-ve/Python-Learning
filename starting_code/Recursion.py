# FActorial Question is on eof the example of recurion 

# def factorial(num):
#     if(num==1 or num == 0):
#         return 1
#     else:
#         return(num* factorial(num-1))

# num =  int(input("Enter the number: "))
# print("Number is: ", num)
# print("Faxtorial of that number is : ", factorial(num))



# Fibonaaci Series 

def fib(num):
    if (num == 0):
        return 0
    elif(num == 1):
        return 1
    else:
        return ((num-1)+(num-2))


num = int(input)