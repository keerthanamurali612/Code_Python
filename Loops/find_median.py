# Write a Python program to find the median of three values.
# Expected Output:
# Input first number: 15
# Input second number: 26
# Input third number: 29
# The median is 26.0


x=input("enter the first num")
y=input("enter the second num")
z=input("enter the third num")

print("Median of the above three numbers -")

if y < x and x < z:
    print("the first num1 :",x)
elif z < x and x < y:
    print("the first num2 :",x)
elif z < y and y < x:
    print("the second num1 :",y)
elif x < y and y < z:
    print("the second num2 :",y)
elif y < z and z < x:
    print("the third num1 :",z)
elif x < z and z < y:
    print("the third num2 :",z)



