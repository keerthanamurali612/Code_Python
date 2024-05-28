#Calculate the product of elements in a list using a for loop:

list=[2,7,3]
def multiply(list):
    for i in list:
        product = product * i
        print(f"The product of elements in a list : {product}")

product=multiply()
