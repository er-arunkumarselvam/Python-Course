# Bubble Sort
arr = [2,18,6,10,4,7,1]
for i in range(3):
    print(arr[i],end=" ")
print()
for j in range(0,3):
    print(arr[j],end=" ")
print()
array = [5,3]
print("Before Swapping : ",array)
if array[0] > array[1]:
    array[0],array[1] = array[1],array[0]
    print("After Swapping : ", array)
for i in range(10):
    print(i)
    break
    print()
# Find Biggest among the given number
n = len(arr)-1
print("Before Swapping : ", arr)
for j in range(0,n):
    for i in range(0, n):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
print("After Swapping : ", arr)
print("Biggest Number is : ",arr[-1])
n = n-1
# Find Second Biggest among the given number
print("Before Swapping : ", arr)
for j in range(0,n):
    for i in range(0, n):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1], arr[i]
print("After Swapping : ", arr)
print("Second Biggest Number is : ", arr[-2])
n = n-1
print()
# Insertion Sort
arrayList = [10, 2, 5, 3, 6, 4, 1, 7, 9, 8]
print("Before Selection Sort : ", arrayList)
n1 = len(arrayList)-1
for j in range(0,n1):
    for i in range(0,n1):
        if arrayList[i] > arrayList[i+1]:
            arrayList[i], arrayList[i+1] = arrayList[i+1], arrayList[i]
print("After Selection Sort : ", arrayList)
n1 = n1-1
print()
# Selection Sort
A = [65, 25, 12, 22, 11]
print("Before Selection Sort : ", A)
n2 = len(A)
for i in range(0, n2):
    min_number = i
    for j in range(i+1,n2):
        if A[min_number] > A[j]:
            min_number = j
            A[i], A[min_number] = A[min_number], A[i]
print("After Selection Sort : ", A)
print()
n2 = n2+1



