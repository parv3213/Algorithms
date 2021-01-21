#Python3 Quick Sort

def partition(arr, l, r):
    pivot = arr[l]
    i = l+1
    j = r

    while(i < j):
        while(pivot >= arr[i] and i <= r): i += 1
        while(pivot <= arr[j] and j > l): j -= 1
        if (i < j): arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j

def quickSort(arr, l, r):
    if l < r:
        pi = partition(arr, l, r)
        quickSort(arr, l, pi-1)
        quickSort(arr, pi+1, r)

# driver code
arr = [10, 80, 5, 90, 40, 50, 70]
quickSort(arr, 0, len(arr)-1)
print (arr)

