from time import *
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
              error= error+1
        except:
            error = error+1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed) 
while True:
    ck = input("Ready to test your Speed:")
    if ck == "yes":
          test = ["In this typing speed test game using Python ","tutorial, you will learn how to check the speed.", " If you know the basics of Python and the pygame library, you can easily calculate the speed"]
          test1 = r.choice(test)
          print("  ******Typing speed*********  ")
          print(test1)
          print()
          print()
          time_1 = time()
          testinput = input("Enter: ")
          time_2 = time()
          print('Speed : ' ,speed_time(time_1, time_2, testinput), "w/sec")
          print("Error : ",mistake(test1, testinput))
    if ck == "no":
        print("THank You for your time")
        break
    
    else:
        print("Please Enter the valid input")