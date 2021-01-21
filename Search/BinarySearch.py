# Python3 for recursive binary search
# If found return index, else returns -1
import math
def binarySearch(arr, l, r, x):
	if l <= r:
		m = (l + (r)) // 2
		if arr[m] == x:
			return m
		elif arr[m] > x:
			return binarySearch(arr, l, m-1, x)
		else:
			return binarySearch(arr, m+1, r, x)
	else:
		return -1

def binarySearch2(arr, n, x):
	r = n - 1
	l = 0
	while (l <= r):
		mid = (l + r) // 2
		print (l,r, mid)
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			r = mid - 1
		else :
			l = mid + 1
	return -1

# Driver Code 
arr = [2, 3, 4, 10, 40] 
x = 3
n = len(arr) 

for i in arr:
	# Function call 
	result = binarySearch2(arr, n, i) 
	if(result == -1): 
		print("Element is not present in array") 
	else: 
		print("Element is present at index", result)