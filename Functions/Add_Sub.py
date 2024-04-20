#Exercise 2: Return multiple values from a function

def add_sub(num1,num2):
    add=num1+num2
    sub=num1-num2

    return add,sub


res= add_sub(40,10)
print(res)