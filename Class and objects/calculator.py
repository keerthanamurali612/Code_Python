#Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

class Calculate:

    def add(num1,num2):
        return num1+num2
    def sub(num1,num2):
        return num1-num2

    def mul(num1, num2):
        return num1 * num2

result1=Calculate.add(60,20)
result2=Calculate.sub(60,20)
result3=Calculate.mul(60,20)

print("The addition is:",result1)
print("The Subtraction is:",result2)
print("The Multiplication is:",result3)
