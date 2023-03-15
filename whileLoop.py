# Number in reverse order
lastDigit = int(input("Please, Enter Last Digit : "))
while lastDigit>= 0:
    print(lastDigit )
    lastDigit -= 1
# Number in Front order
lastDigit = int(input("Please, Enter Last Digit : "))
first=1
while first<=lastDigit:
    print(first)
    first+=1
# Print 0-100 even numbers only
first=0
while first<=100:
    print(first)
    first+=2
# Print 1-100 odd numbers only
first = 1
while first <= 100:
    print(first)
    first += 2
# Print multiple of 3 only
first = 1
last=100
while first <= last:
    if first%3==0 :
        print("Multiple of 3 : ",first)
    first+=1
# Print multiple of 3 only
first = 3
last=100
while first <= last:
    print("Multiple of 3 : ", first)
    first += 3
#print power of 3 only
first = 3
last=100
while first <= last:
    print("Power of 3 : ", first)
    first *= 3
# print 1-100 between divisible 2 or 3
first=1
last=100
while first <=last:
    if (first%2==0 or first%3==0):
        print(first)
    first+=1
# print 1-100 between divisible 2 and 3
first=1
last=int(input("Enter the range of number : "))
while first <=last:
    if (first%2==0 and first%3==0):
        print(first)
    first+=1
# Sum of 1-10
first=1
last=10
total=0
while first<=last:
    total+=first
    first+=1
print(total)
# multiply of 1-10
first=1
last=10
total=1
while first<=last:
    total*=first
    first+=1
print(total)

