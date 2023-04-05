#8,7,6,1,0,9,2
def partition(array, low, high):
    pivot = array[high]
    i = low - 1#i=-1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
            #swap the pivot element with the greater element specified be 2
    (array[i+1], array[high]) = (array[high], array[i+1])
    return i + 1
#function to perform quicksort
def quickSort(array, low, high):#low=0 high=6
    if low < high:
        pi = partition(array, low, high)#pi=2
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
data=[8,7,6,1,0,9,2]
print("Unsorted Array:")
print(data)
size=len(data)
quickSort(data,0,size-1)
print("Sorted Array in Ascending Order:")
print(data)
    
