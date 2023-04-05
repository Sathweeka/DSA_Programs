def selectionSort(array, size):
    for step in range(size):
                            #step =0 [20, 12, 10, 15, 2]step
                            # step =1 [2, 12, 10, 15, 20]step
                            # step =2 [20, 10, 12, 15, 2]step
                            #step =3 [12, 10, 15, 2]step
        min_idx = step#min_index=1
        for i in range(step + 1, size):
            #to sort in descending order, change > to < in this
            #select the minimum element in each loop
            if array[i] < array[min_idx]:#20<10
                min_idx = i#2
                #put min at the correct position
            (array[step], array[min_idx]) = (array[min_idx], array[step])
data = [20, 12, 10, 15, 2]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)
            
        
