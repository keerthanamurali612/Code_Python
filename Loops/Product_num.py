#Calculate the product of elements in a list using a for loop:

# list=[2,3,4]
# product=2
#
# for i in list:
#     total=product * i
#
# print(total)


def multiply(list):
    for i in list:
        result = result * i
        return result



num=multiply(list=[2,7,3])
print(num)