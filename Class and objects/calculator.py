#Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

class Calculate:

    def add(self,num1,num2):
        return num1+num2
    def sub(self,num1,num2):
        return num1-num2

    def mul(self,num1, num2):
        return num1 * num2

    def div(self,num1,num2):
        if num2!=0:
            return num1%num2
        else:
            return "can't divide zero"



calculate=Calculate()

result1=calculate.add(60,20)
result2=calculate.sub(40,10)
result3=calculate.mul(30,20)
result4=calculate.div(30,20)

print("The addition is:",result1)
print("The Subtraction is:",result2)
print("The Multiplication is:",result3)
print("The Divison is:",result4)
