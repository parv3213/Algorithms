# Python3 for Merge Sort

def mergeSort (arr) :
    if len(arr) > 1:
        mid = (len(arr))//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            k += 1
            i += 1
        while j < len(R):
            arr[k] = R[j]
            k += 1
            j += 1

#driver code
arr = [38, 27, 43, 3, 9, 82, 10] 
print ("Sorted Array:")
mergeSort(arr)
print (arr)