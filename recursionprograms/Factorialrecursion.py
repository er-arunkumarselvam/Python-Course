# # Find the factorial using recursion
def fact(number):
    if number == 0:
        return 1
    else:
        return number * fact(number-1)
print(fact(0)) # composition of function
print(fact(5))

