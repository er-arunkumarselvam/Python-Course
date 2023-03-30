"""#sum of first numbers
no=1
total=0
for no in range(11):
    total=total+no
print("First n numbers values is : ",total)
#sum of n numbers in user input
total=0
number=int(input("Enter a any number : "))
for i in range(number+1):
    total+=i
print("First n numbers values is : ",total)
#sum of range of numbers
total=0
for no in range(5,20):
    total+=no
print("Total a range of numbers 5 to 20 is : ",total)
#sum of range of numbers
total=0
firstNumber=int(input("Enter a first number : "))
secondNumber=int(input("Enter a second number : "))
for no in range(firstNumber,secondNumber+1):
    total+=no
print("Total a range of numbers",firstNumber," to", secondNumber," is : ",total)
#sum of number using step up
total=0
for no in range(5,20,2):
    total+=no
print("Total a range of numbers 5 to 20  with step 2 is : ",total)"""
#print odd number only
print("Odd Numbers Only : ")
for i in range(101):
    if (i%2!=0):
        print(i,end=" ")
    i+=1
print()
#print even number only
print("Even Numbers Only : ")
for i in range(101):
    if (i%2==0):
        print(i,end=" ")
    i+=1
print()
# print multiples of 3 only
print("Multiples of 3 Only : ")
for i in range(1,101):
    if (i % 3== 0):
        print(i, end=" ")
    i += 1
print()
# print multiples of 3 only using step operation
print("Multiples of 3 Only using step operation : ")
for i in range(3,101,3):
        print(i, end=" ")
print()
#Palindrome
word="madams"
word2=word[::-1]
if word==word2:
    print("The given word",word,"is palindrome")
else:
    print("The given word",word,"is Not palindrome")

