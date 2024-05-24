#Count the number of even and odd numbers from a series of numbers


a=[1,2,3,4,5,6,7,8,9]
even_count=0
odd_count=0
for i in a:
    if i%2==0:
        even_count=even_count + 1
    else:
        odd_count=odd_count +1


print("The even numbers is :",even_count)
print("The odd numbers is :", odd_count)








