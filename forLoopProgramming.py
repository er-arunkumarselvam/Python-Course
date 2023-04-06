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
print("Total a range of numbers 5 to 20  with step 2 is : ",total)
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
    print("The given word",word,"is Not palindrome")"""

#sentence
sentence ="All is Well"
for letter in sentence:
        print(letter,end=" ")
print()
#sentence find vowls
sentence ="All is Well"
for letter in sentence:
    if letter in ['a','e','i','o','u','A','E','I','O','U']:
        print(letter,end=" ")
print()
#find the no. of words
sentence="My name is Arunkumar"
count=1
space=" "
for letter in sentence:
    if letter in space:
        count+=1
print("No. of words present is : ",count)
#find the no. of sentence
sentence="My name is Arunkumar. I completed BE. I am from Kumbakonam."
count=0
for letter in sentence:
    if letter ==".":
        count+=1
print("No. of sentence present is : ",count)
print()
#print capital letter using ord()
for letter in range(ord('A'),ord('Z')+1):
    print(chr(letter),end=" ")
print()
# print capital letter using ASCII value
for letter in range(65, 91):
    print(chr(letter), end=" ")
print()
#using pass
for number in [1]:
    pass
print("Hello",number)