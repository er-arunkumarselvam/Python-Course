# Linear Search
rollNoList = [101, 103, 105, 104, 540, 985, 410, 110, 546, 666]  # List
print("Hall 01 : ", rollNoList)
yourRollNo = int(input("Enter your Roll No : "))

index=0
flag = 0 # count = 0
while index < len(rollNoList):
    if rollNoList[index] == yourRollNo:
        flag =1
        break
    index += 1
if flag ==1:
    print("Your Roll Number Position is ", index+1)
else:
    print("Your Roll Number is not present in the hall.")