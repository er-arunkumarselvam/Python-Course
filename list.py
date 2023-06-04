# append() and remove functions
alpha = ['a', 'b', 'c', 'd']
alpha.append('e')
print(alpha)
alpha.remove('d')
print(alpha)
listA= [['a', 'b', 'c'],[1 ,2 ,3], 'D']
listA.remove([1,2,3])
print(listA)
print()
#  Find the Square Numbers from user given number
number = int(input("Enter a any number : "))
squares = []
for num in range(1, number+1):
    squares.append(num*num)
print(squares)
print()
# List Comprehension
squares = [num*num for num in range(10)]
print(squares)
print()
# Duplicate Elements Find and Remove
# count() above 1 is duplicate element
# remove the duplicate element
bike =["Hero", "Yamaha", "Honda", "KTM", "TVS",  "Honda"]
print(bike)
print(bike.count('Honda'))
bike.remove("Honda") #Remove starts from left side
print(bike)
print()
#reverse function
bike =["Hero", "Yamaha", "Honda", "KTM", "TVS",  "Honda"]
print(bike)
print(bike.count('Honda'))
bike.reverse()
bike.remove("Honda") #Remove starts from Right side
print(bike)
print()
# Index Method
foods = ['Idly', 'Dosa', 'Pongal', 'Chappathi', 'Idly']
value = foods.index('Idly')
print(value)
value = foods.index('Idly', 2)
print(value)
foods.insert(4, 'Masala Dosa')
print(foods)
value = foods.index('Idly', 2)
print(value)