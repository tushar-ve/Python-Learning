# DIctornary 
# Dictionary can contain duplicacy
indo = {223:"Rahul",
        224:"Tushar",
        225: "Neha",
        226: "Ashwani"}
print(indo)
print(indo.keys())
print(indo.values()) 

if 223 in indo:
    print("present")
else:
    print("Absent")    



# here we are getting all the keys 

# for key in indo.keys():
#     print(indo[key])

# if we want to get all values


# print(indo.items())
# for key, value in indo.items():
#     print(f"The key value corresponding to the {key} is {value}")


# d = {i:('even' if i%2 == 0 else 'odd') 
#      for i in range(1,11)}
# print(d)

#Updated method
ep1 = { 233: 90, 234: 98, 123:22, 121:22}
ep2= {223:91, 235:88, 390:33}
# ep1.update(ep2)
# print(ep1)

# ep1.clear()
# popitem() will remove last element from the dictinoary 
# pop() can remove the inserted value key 
ep1.pop(123)
print(ep1)
ep1.popitem()
print(ep1)

tel = {'jack': 4198, 'sape': 4139}
tel['yuido'] = 4127


# This is how we can add the element 
del tel['sape']
print(tel)
sorted(tel)


print({x: x**2 for x in (2, 4, 6)})


# Looping Techniques

# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#     print(k, v)


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {1}? \n It is {1}.'.format(q, a))




