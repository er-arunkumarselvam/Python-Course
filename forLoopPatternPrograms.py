#print pattern program
for row in range(1,6):
    for col in range(1,6):
        print(row,end=" ")
    print()
print()
for row in range(1,6):
    for col in range(1,6):
        print(col,end=" ")
    print()
print()
for row in range(1,6):
    for col in range(1,6):
        print(1,end=" ")
    print()
print()
for row in range(1,6):
    for col in range(1,6):
        print("*",end=" ")
    print()
print()
for row in range(65,70):
    for col in range(65,70):
        print(chr(row),end=" ")
    print()
print()
for row in range(1,6):
    for col in range(0,row):
        print(row,end=" ")
    print()
print()
for row in range(1,7):
    for col in range(1,row):
        print(col,end=" ")
    print()
print()