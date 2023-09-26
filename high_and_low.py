

def high_and_low(numbers):
    data=list(int(i) for i in numbers.split(' '))
    output = f'{max(data)} {min(data)}'
    return output

print(high_and_low('1 2 3 4 5'))

