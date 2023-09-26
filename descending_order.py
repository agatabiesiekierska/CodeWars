'''
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. 
Essentially, rearrange the digits to create the highest possible number.
'''
def descending_order(num):
    digits = [i for i in str(num)]
    digits.sort(reverse = True)
    number = str().join(i for i in digits)
    return int(number)

print(descending_order(123456789))

    