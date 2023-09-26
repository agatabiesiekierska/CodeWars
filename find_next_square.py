'''
Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. 
Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.
'''
from math import sqrt
def find_next_square(sq):
    if sqrt(sq).is_integer():
        value = int(pow(((sqrt(sq))+1),2))
        return print(f'{sq} --> {value}')
    else: return print(f'-1, since {sq} is not a perfect square!')

    