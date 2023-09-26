'''
Define a function that takes an integer argument and returns a logical value true or false depending on if the integer is a prime.
'''
import math
def is_prime(num):
  if num <= 0 or num == 1: return False
  elif num == 2: return True
  else:
    for i in range (2, int(math.sqrt(num))+1):
      if num % i == 0: return False
    return True

try:
  n = float(input('Please, enter your number: '))
  print('If the number is prime: ',is_prime(n))

except Exception as e:
  print(f'Ups! There is an error...\n Details: {e}')