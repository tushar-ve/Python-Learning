

# str2 = "hardik"
# print(len(str2))
# str1 = list(str2)
# print(str1)
# str1.reverse()
# print(str1)
# print(" ".join(str1))

# //With help of abhishek 


str2 = "Hello here is he"

str2.split()
x = []
for i in range (len(str2)):
    if(i == 0):
        x.append(str2[-1])
    elif(i == len(str2)-1):
        x.append(str2[0])
    if(i !=0 and i!=len(str2)-1):
        x.append(str2[i])
str2= " ".join(x)
print(str2)