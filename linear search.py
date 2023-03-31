#linear search in python
# here time complexity is more: O(n)
def linearSearch(array, n, x):
    # Going through array sequentially
    for i in range(0, n):#0 to 4
        if(array[i] == x):
            return i
    return -1
array = [2,4,0,1,9]
x = 1#key
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)
