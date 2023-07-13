# Binary Search
number = [1, 10, 20, 30, 40, 55, 60, 70, 85]  #Length = 9
# Index =  0   1   2    3    4    5    6   7    8
x = 10
start = 0
end = len(number) - 1  # 9-1=8, 3
while end >= start:  # True
    mid = start + (end - start) // 2  # 0+(8-0) //2 = 4, 0+(3-0) //2 = 1
    if number[mid] == x:  # number[4] =40 == 10 (Not), number[1] = 10 == 10
        result = mid  # 1
        break
    elif number[mid] > x:  # number[4] = 40 > 10,
        end = mid - 1  # end = 4-1 = 3
    else:
        start = mid+1
else:
    result = -1

if result != -1:
    print("Element is present at the index", result)
else:
    print("Element is not present at the index")
