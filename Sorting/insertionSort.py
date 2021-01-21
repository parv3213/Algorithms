# Insertion Sort

def insertionSort (arr):
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            key = arr[i]
            j = i-1
            while j>=0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
    return arr

# Driver code
arr = [64, 34, 25, 12, 22, 11, 90] 
print ("Sorted Array:")
arr = insertionSort(arr)
print (arr)