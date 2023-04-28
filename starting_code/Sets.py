# Day-3 Started python video-31


#  Set is a unoredred  collection of data items 
# We cannnot access the set using index number 

tushar = {"hello", 88, 9.098, 98, 88}
print(tushar)
h = { "hello", 88}
print(h)
# for value in tushar:
#     print(value)  
# set is getting updated with the other set value when w use update function
# tushar.update(h)
# print(tushar)
# union is use to make the union in the set got printed 
# print(h.union(tushar))

# 

# Intersection is used to get the common value in between 
# print(h.intersection(tushar))

# intersection_update is used to update value in a particular set 

# tushar.intersection_update(h)
# print(tushar)

# symmetric_difference is used to know the symmwtric difference between to sets 
# tushar.symmetric_difference_update(h)
# print(tushar)

# Check the element disjoint 

# print(tushar.isdisjoint(h))

# superset check 
print(tushar.issuperset(h))

# Check the subset 
print(h.issubset(tushar))

# add the value at the end 
h.add("new-word")
print(h)

# remove/discard is use to remove the item from the list 
h.discard(88)
print(h)

# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)

# remove multiple element form set 
# set1 = {10, 20, 30, 40, 50}
# set1.difference_update({10, 20, 30})
# print(set1)