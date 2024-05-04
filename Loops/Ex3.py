# Given two integer numbers, return their product only if the product is equal to or lower than 1000.
# Otherwise, return their sum.

number1=80
number2=30

res=number1*number2

if res<1000:
    print("The result is ",res)
else:
    print("The result is ",number1+number2)