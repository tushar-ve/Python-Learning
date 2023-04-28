# raise keyword is use to raise error 
# a = int((input("Enter any value between 5 & 9:")))
# if(9>a<5):
#     raise ValueError("Value should be between 4 & 9")

# for a string

a = input("Enter your string: ")

if(a!="quit"):
    raise ValueError("invalid string")
else:
    print("string is valid")