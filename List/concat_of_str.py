# Exercise 3: Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
res = [x + y for x in list1 for y in list2]
print(res)