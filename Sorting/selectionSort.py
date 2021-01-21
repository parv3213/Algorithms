# Selection Sort
# sort an array using selection sort

def selectionSort (arr) :
    for i in range(0, len(arr)):
        minEl = i
        for j in range(i, len(arr)):
            if (arr[j] < arr[minEl]):
                minEl = j
        if minEl != i:
            arr[i], arr[minEl] = arr[minEl], arr[i]
    return arr


# Example code
arr = [64, 25, 12, 22, 11] 
print ("Sorted Array:")
arr = selectionSort(arr)
print (arr)