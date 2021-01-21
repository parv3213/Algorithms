#Bubble sort
def bubbleSort(arr):
    for i in range(0, len(arr)-1): #max no of iterations 
        swapped = False
        for j in range(0, len(arr)-1): #max no of swaps
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if swapped == False:
            break
    return arr

# Driver code
arr = [64, 34, 25, 12, 22, 11, 90] 
print ("Sorted Array:")
arr = bubbleSort(arr)
print (arr)