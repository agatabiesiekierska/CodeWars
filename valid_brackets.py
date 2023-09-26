# Work in progress
'''
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
'''

def valid_brackets(string):
    val = True
    data = list(str(i) for i in string)
    if len(data) % 2 != 0: return False
    for i in range(int(len(data)/2),2):
        new_string = str(data[i] + data[i+1])
        if not (new_string == r'{}' or new_string == r'()' or new_string == r'[]'):
            val = False
            break
    return val
            

print(valid_brackets(r"[({})](]"))
