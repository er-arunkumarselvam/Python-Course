# Exception Handling
x=int(input("enter your no1: "))
y=int(input("enter your no2: "))
print(x/y) # infinity
# ZeroDivisionError: division by zero
# put y value is any str --> ValueError: invalid literal for int() with base 10: 'x'
x = int(input("enter your no1: "))
y = int(input("enter your no2: "))
try:
    print(x / y)
except (ZeroDivisionError) as msg:
    print(msg)
except ValueError as msg:
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
file =open(r'/home/arun/Music/python/ExceptionHandling/pincodes.txt')
for each_line in file:
    (city,pincode) = each_line.split("-")
    print("pincode of",city,end="")
    print("is",pincode,end="")
file.close()

