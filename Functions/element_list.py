#Calculate the product of elements in a list using a for loop:


def multiply(list):
    for i in list:
        result = result * i
        print(f"The product of elements in a list : {result}")

num=multiply(list=[2,7,3])
print(num)