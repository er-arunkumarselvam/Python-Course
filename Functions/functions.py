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
print()


# Default Argument
def find_discount(mrp, discount_percentage=10):  # Default Argument 10 in this case
    discount = mrp ** (discount_percentage / 100)
    discount_price = mrp - discount
    print(round(discount_price, 2))


# Functions Calling Statements
find_discount(100)
find_discount(100, 25)  # Change the argument 25 in this case
print()


def find_discount(mrp, discount_percentage):
    discount = mrp ** (discount_percentage / 100)
    discount_price = mrp - discount
    print(round(discount_price, 2))


# Functions Calling Statements
find_discount(mrp=100, discount_percentage=25)
find_discount(discount_percentage=25, mrp=100)
print()


# Keyword Arguments
def tellMeYourName(*names):  # Passing to parameters. it denoted by *.  - DataType is Tuple
    for name in names:
        print(name, end="  ")

print()
tellMeYourName('Arun', 'Shafik', 'Dharma', 'Vinith', 'Vignesh')



# Variable length Arguments
def totalPrice(sellingPrice, buyingPrice):
    print(sellingPrice)
    print(buyingPrice)

print()
totalPrice(100, 90)  # Two Arguments was passed


def totalPrice(*amount):  # Get all the parametes using variable length argument - DataType is Tuple
    for cash in amount:
        print(cash)

print()
totalPrice(100, 90, 5, 5)  # sellingprice = 100, buyingprice = 90, SGST = 5, CGST = 5
