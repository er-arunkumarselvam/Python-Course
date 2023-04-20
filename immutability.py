# Task-1
from typing import List

house_no=10
print(type(house_no))
print(id(house_no))#Id
house_no=12
print(id(house_no)) #Id Changed
print()
# Task-2
mark=75
print(id(mark))
mark=mark+10
print(id(mark))
print()
# Task-3
count=0
print(id(count))
count+=1
print(id(count))
print()
# Task-4 - Strings
captain="Dhoni"
print(id(captain))
captain="Kolhi"
print(id(captain))
print()
# Task-5 - Immutable
city1="kumbakonam"
city2="kumbakonam"
print (city1 is city2)
print (city1==city2)
print(id(city1))
print(id(city2))
print()
# Task-6
# name='Raja'
# name[1]='o'
# print(name) # Traceback- TypeError: 'str' object does not support item assignment
# print()
#Task-7 - change letters
name='class'
print('g'+name[1:])
print()
# List (Mutable) => Only value changed not change memory address
list=['arun',503,7.54,True]
print(id(list))
list[0]='arunkumar'
print(id(list))

