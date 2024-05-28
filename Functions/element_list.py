#Calculate the product of elements in a list using a for loop:


def multiply(list):
    product=1
    for i in list:
        product = product * i
    return product


#create a list
list=[1,2,7,3,5]

#create an object
product=multiply(list)

#print the product
print(f"The product of elements in a list : {product}")


