#print pattern programs
row=1
while row<=5:
    col = 1
    while col<=5:
        print(row,end=" ")
        col+=1
    print()
    row+=1
print()
row=1
while row<=5:
    col = 1
    while col<=5:
        print(col,end=" ")
        col+=1
    print()
    row+=1
print()
row=1
while row<=5:
    col = 1
    while col<=5:
        print(1,end=" ")
        col=col+1
    print()
    row+=1
print()
row=1
while row<=3:
    col = 1
    while col<=5:
        print(col,end=" ")
        col=col+1
    print()
    row+=1
print()
row=1
while row<=3:
    col = 1
    while col<=row:
        print(row,end=" ")
        col=col+1
    print()
    row+=1
print()
row=1
while row<=5:
    col = 1
    while col<=row:
        print(col,end=" ")
        col=col+1
    print()
    row+=1
print()
row=1
while row<=5:
    col=5
    while col>=6-row:
        print(col,end=" ")
        col-=1
    print()
    row+=1
print()
row=1
value=65
while row<=5:
    col=1
    while col<=row:
        print(chr(value),end=" ")
        col+=1
    print()
    row+=1
print()
row=1
value=65
while row<=5:
    col=1
    while col<=row:
        print(chr(value),end=" ")
        value+=1
        col+=1
    print()
    row+=1
print()
row=1
value=65
while row<=5:
    col=1
    while col<=row:
        print(chr(value),end=" ")
        col+=1
    print()
    value += 1
    row+=1
print()
row=1
value=65
while row<=5:
    col=1
    while col<=row:
        print(chr(value),end=" ")
        value += 1
        col+=1
    print()
    value=65
    row+=1
print()
row=1
while row<=5:
    col=1
    while col<=row:
        print("*",end=" ")
        col+=1
    print()
    row+=1
print()
row=5
while row>=1:
    col=1
    while col<=row:
        print("*",end=" ")
        col+=1
    print()
    row-=1
print()
name="Arunkumar"
count=len(name)
for terms in range(count):
    for letter in range(count):
        print(name[letter],end=" ")
    print()
    count-=1
print()
count=5
terms=0
for terms in range(count):
    for row in range(count):
        print(" ",end=" ")
    for col in range(terms+1):
        print("*",end=" ")
    print()
    count-=1
print()
count=5
terms=0
for terms in range(count):
    for row in range(count):
        print(" ",end=" ")
    for col in range(terms+1):
        print("*  ",end=" ")
    print()
    count-=1
print()
count=5
terms=0
for terms in range(count):
    for row in range(count):
        print(" ",end=" ")
    for col in range(terms+1):
        print(chr(col+65),end="   ")
    print()
    count-=1
print()
count=5
terms=0
for terms in range(count):
    for row in range(count):
        print(" ",end=" ")
    for col in range(terms+1):
        print(chr(col+65),end=" ")
    print()
    count-=1
print()