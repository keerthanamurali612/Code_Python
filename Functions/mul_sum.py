#Calculate the multiplication and sum of two numbers


def mul_sum(number1,number2):
    product=number1*number2

    if(product<1000):
        return  product
    else:
        return number1+number2

result1=mul_sum(20,30)    #less than 1000 means results is product of 2 numbers
result2=mul_sum(60,30)    #greater than 1000 means results is sum of  2 numbers

print("The result is",result1 )
print("The result is",result2 )