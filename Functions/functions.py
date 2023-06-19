# sum()
def sum(number1, number2):
    return number1 + number2  # True or False


result = sum(10, 20)
print(result)
print()


# palindrome()
def palindrome(word):
    return word == word[::-1]  # Slicing Operator used and Step


# For understanding purpose in above line
#     print(word[::-1])
#     reversedWord = word[::-1]
#     if word == reversedWord:
#         return True
#     else:
#         return False
#     return word == word[::-1]


word = input("Enter your word : ")
if palindrome(word):  # Function Calling
    print(word, " is palindrome.")
else:
    print(word, " is not palindrome.")
print()


# Scope of Variables
# Local Variables is used for particular function.
# Global Variables is used for All functions.
def getChange(money):  # argument
    money = 2000  # Local Variable
    print("Change the money.", money)


money = 10000  # Global Variable
print("To be spent money is ", money)
getChange(money)  # Function Calling - Parameter
print("Change the money.", money)
print()

# Global Keyword
price = 1  # Global Variable
print(price)


def calculate():
    global price  # Global Keyword used for explicit change the price value in below line. Directly not change in price value got below error
    price += 2
    # price =price+2  - Editing the Global Variable (3)
    # UnboundLocalError: cannot access local variable 'price' where it is not associated with a value
    print(price)
    print(price + 2)  # for adding to printing along with global variable (1+2=3)


calculate()
print(price)
print()

#  Local vs Global
x = 8


def loc():
    x = "Local"
    print("Local x Value is ", x)
    print(id(x))


loc()
print("Global x Value is ", x)
print(id(x))