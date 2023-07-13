file = open("D:\\Practice\\Python-Course\\fileHandling\\test", "w")
print("File name is ", file.name)
print("File mode is ", file.mode)
print("File Property is ", file.readable())
print("File Property is ", file.writable())
print("File is closed or not - ", file.closed)
file.close()
print("File is closed or not - ", file.closed)
file = open("D:\\Practice\\Python-Course\\fileHandling\\test", "a")
print("File is closed or not - ", file.closed)
# writing a file
file.write("Arunkumar")
file.write(" is a mechanical engineer.\n")
list = ["Arunkumar\n", "Shafik\n", "Dharma\n", "Vinith\n", "Vignesh\n"]
file.writelines(list)
file.close()
# reading a file
file = open("D:\\Practice\\Python-Course\\fileHandling\\test", "r")
print("File is closed or not - ", file.closed)
# read a file
# output = file.read()
# outputChange = file.read(5)  # first 5 characters
# lineRead = file.readline()  # read single line
linesRead = file.readlines()  # read entire line - datatype is List

# print(output)
# print(outputChange)
# print(lineRead)
print(linesRead)
print("Before Changing ", type(linesRead))
changelinesRead = str(linesRead)
print("After Changing ", type(changelinesRead))
# If remove the \n or commas using join function
information = " ".join(linesRead)
print(information)
print(type(information))
file.close()
print()

# With  Statement - to avoid the open and close the file in every time
with open("D:\\Practice\\Python-Course\\fileHandling\\test", "r") as file:
    print("File is closed or not - ", file.closed)
    # read a file
    print(file.tell())
    output = file.read(9)
    print(output)
    print(file.seek(10))
    print(file.tell())
    output = file.read(15)
    print(file.tell())
    print(output)
print()

# If file is present or not in the directory
import os

filename = input("Enter your file name : ")
if os.path.isfile(filename):
    print("Yes, File is present.")
    with open(filename, "r") as file:
        print(file.read())
else:
    print("No, File is not present.")
print()

# Open Binary Files
binaryFile1 = open(r"D:\Practice\Python-Course\fileHandling\imageFile.jpg", "rb")
binaryFile2 = open(r"D:\Practice\Python-Course\fileHandling\imageFile-copy.jpg", "wb")
binaryFile3 = open(r"D:\Practice\Python-Course\fileHandling\imageFile-copy1.jpg", "wb")
data = binaryFile1.read()
binaryFile2.write(data)
binaryFile1.close()
binaryFile2.close()
binaryFile3.close()
print()

# CSV File Handling
import csv

with open(r"D:\Practice\Python-Course\fileHandling\productDetails.csv", "w") as cFile:
    write = csv.writer(cFile)
    write.writerow(["Product.Id", "Product Name", "Price"])
    no = int(input("Enter the no. of products : "))
    for productItems in range(no):
        prodId = int(input("Enter a Product Id : "))
        prodName = input("Enter a Product Name : ")
        prodPrice = int(input("Enter a Product Price : "))
        write.writerow([prodId, prodName, prodPrice])
