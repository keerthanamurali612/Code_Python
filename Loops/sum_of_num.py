#Exercise 2: Calculate the sum of all numbers from 1 to a given number

sum=0
num=int(input("enter the number"))
for i in range(1,num+1):
    sum=sum+i

print(sum)