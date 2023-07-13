# Lists
squares=[1, 4, 9, 16, 25]
print(squares[0])
print(squares[-1])
print(squares[-3:])
print(squares[:])
squares1 = [36, 49, 64, 81, 100]
total=squares+squares1 #list concatenation
#squares+[36, 49, 64, 81, 100] is it same answer
print(total)
#list is mutable
squares[3]=12
print (squares)#befor list squares[3]=16 after squares[3]=12
#append() function
total.append(121)
total.append(12**2)
print(total)
#append() list and list values
letter=['a','b','c']
squares.append(letter[0])
print(squares)
squares.append(letter)
print(squares)
# slicing operator using change list member
letter[1:2]=['B']
print(letter)
# Remove all list members
letter[:]=[]
print(letter)
letter=['a','b',"c"]
# length of list
print(len(letter))
#list+list
alpha=['a','b']
number=[1,2]
both=alpha,number
print(both)
print("Lenght of Both is " ,len(both))
print(both[0])
print(both[1])
print(type(number))
print(type(alpha))
print(type(both))
print(type(both[0]))
print(type(alpha[0]))
print(type(number[0]))
print(both[0][0]) # both first [0] indicates first list , both second [0] indicates inside the list index (first list first member)
print(both[0][1])
print(both[1][0])
print(both[1][1])
# Printing list using for loop
listedItems=['Idly','Dosa','Pongal','Poori','Vada']
for items in listedItems:
    print(items,end=" ")
    print()
# Printing combined list
for listItem in both:
    for listMembers in listItem:
        print(listMembers, end=" ")
    print()
# print alphabetical letters only
for listItem in both:
    for listMembers in listItem:
        print(listMembers,type(listMembers), end=" ")
        print()
for listItem in both:
    for listMembers in listItem:
        # if listMember.isalpha():
        if type(listMembers)==str:
            print(listMembers, end=" ")
    print()
# Print While Loop
alpha=['c','a','b','c']
number=[1,2,4,3]
both=[alpha,number]
li=0
while li<len(both): #li=0 < len(both)=2
    item=0
    while item<len(both[li]): # item=0 both[li]=4
        print(both[li][item],end=" ") # both [0] [0]
        item+=1
    print()
    li+=1
print()
# Print only alphabets
alpha=['c','a','b','c']
number=[1,2,4,3]
both=[alpha,number]
li=0
while li<len(both):
    item=0
    while item<len(both[li]):
        if type(both[li][item])==str:
            print(both[li][item],end=" ")
        item+=1
    print()
    li+=1
print()
# MicroProgram
hrNames=['Arun','Krishna','Vijay']
developerNames=['Shafik','Dharma','Ajay']
testerNames=['Vinith','Vignesh']
adminNames=['Balaji','Prasanna','Aravind','Vengatesh']
companyEmployees=[hrNames,developerNames,testerNames,adminNames]
li=0
#print all names
while li<len(companyEmployees):
    item=0
    while item<len(companyEmployees[li]):
        print(companyEmployees[li][item],end=" ")
        print()
        item+=1
    print()
    li+=1
print()
#print only names starting letter 'A'
while li<len(companyEmployees):
    item=0
    while item<len(companyEmployees[li]):
        if (companyEmployees[0:])=='A':
            print(companyEmployees[li][item],end=" ")
            print()
        item+=1
    print()
    li+=1
print()