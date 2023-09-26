
def find_uniq(arr):
    arr = list(arr)
    arr.sort()
    if arr.count(arr[0]) == 1:
        return arr[0]
    elif arr.count(arr[len(arr)-1]) == 1:
        return arr[len(arr)-1]

print(find_uniq([1,1,1,2,1,1])) 
print(find_uniq([ 0, 0, 0.55, 0, 0 ])) 