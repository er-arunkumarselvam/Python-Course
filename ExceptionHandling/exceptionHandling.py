# Exception Handling
x=int(input("enter your no1: "))
y=int(input("enter your no2: "))
print(x/y) # infinity
# ZeroDivisionError: division by zero
# put y value is any str --> ValueError: invalid literal for int() with base 10: 'x'

try:
    x = int(input("enter your no1: "))
    y = int(input("enter your no2: "))
    print(x / y)
except (ZeroDivisionError) as msg:
    print(msg)
except (ValueError) as msg:
    print(msg)

# Microprogram
print(arunkumar) # missing single or double quotes
# NameError: name 'arunkumar' is not defined
# MicroProgram
print("Arun"+5) # two str are concatenate
# TypeError: can only concatenate str (not "int") to str
# MicroProgram
file = open("abc.txt")
print(file.read())
# FileNotFoundError: [Errno 2] No such file or directory: 'abc.txt'
# MicroProgram
try:
    print(10/0)
except ZeroDivisionError as msg:
    print(type(msg))
# Microprogram
try:
    print(10/0)
except ZeroDivisionError:
    print(100/5)

# MicroProgram for Exception Handling
def get_number():
    number = int(input("Enter your Pin Number : "))
    return number

while True:
    try:
        print(get_number())
        option = input("Continue? Yes | No")
        if option.lower()== 'no':
            break
    except ValueError:
        print("Please enter valid Pin Number.")

# File Handling Program
file =open(r'/home/arun/Music/python/ExceptionHandling/pincodes.txt')
# print(file.readline(),end="") # Chennai - 600001
for each_line in file:
    print(each_line,end="")
file.close()

# File Handling Program in Exception Handling
try:
    file =open(r'/home/arun/Music/python/ExceptionHandling/pincodes.txt')
    for each_line in file:
        try:
            (city,pincode) = each_line.split("-")
            print("pincode of",city,end="")
            print("is",pincode,end="")
        except ValueError:
            ("Skip the line")
    file.close()
# Default Exception Handling
except:
    print("check the file location")

# FileNotFoundException Handling
try:
    file =open(r'/home/arun/Music/python/ExceptionHandling/pincode.txt')
except:
    print("check the file location")

# One Try multiple except is possible.
try:
    x = int(input("enter your no1: "))
    y = int(input("enter your no2: "))
    print(x / y)
except (ZeroDivisionError):
    print("Please check y value")
except (ValueError):
    print("Enter a valid number ")
except:
    print("Something went wrong")

# Finally
try:
    x = int(input("enter your no1: "))
    y = int(input("enter your no2: "))
    print(x / y)
except (ZeroDivisionError, ValueError) as msg:
    print(msg)
finally:
    print("Finally Check")

# MicroProgram for understandinf of sys class
import sys

inputList = ['a', 0, False, 1, 2, 8, 10]

for entry in inputList:
    try:
        print("The entry is", entry)
        r = 1/entry
        break
    except:
        print("Opps!", sys.exc_info()[0], "occurred.")
        print("Next entry")
        print()
print("The reciprocal of",entry, "is",r)

# MicroProgram
try:
    x = int(input("Enter x value :"))
    y = int(input("Enter y value :"))
    if x>y:
        result =5
        result.append("Hello") # append is attribute for list data type only. can't use append attribute in this line.
    else:
        print("Hi"+5) 
except (AttributeError,TypeError) as error:
    print("The error occurred:",error)
    print("The error occurred:",type(error))