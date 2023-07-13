# Tuple is Immutable
number = (1, 2, 3, 4)
print(type(number))
# number[2] = 10 # TypeError: 'tuple' object does not support item assignment - Can't Change the value - Tuple is Immutable
alpha = ()
print(type(alpha))
alpha = ('a')
print(type(alpha))
alpha = ('a',)
print(type(alpha))
alpha = 'a',
print(type(alpha))
# append,remove - AttributeError: 'tuple' object has no attribute 'append' and 'remove'
# print(alpha.append('b'))
# print(alpha.remove('b'))
paper1 = (1,2,3)
paper2 = (5,7,9)
paper3 = (paper1 , paper2)
print(paper3)
# using concatination - Combained the Tuple
paper3 = (paper1 + paper2)
print(paper3)
#Tuple Packing and Sequence Unpacking
values=10,20,30,40 # Tuple Packing
print(values)
no1,no2,no3,no4 = values # Sequence Unpacking
print("no1 : ",no1)
print("no2 : ",no2)
print("no3 : ",no3)
print("no4 : ",no4)
