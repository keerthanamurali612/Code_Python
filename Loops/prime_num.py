#Exercise 11: Write a program to display all prime numbers within a range

start = 25
end = 50
for i in range(start,end):
    if(i%2!=0 and i%i==0):
        print(i)