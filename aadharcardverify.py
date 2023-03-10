age = int(input("Please Enter your age : "))
if age>5:
    nationality = str(input("Please Enter your Nationality : "))
    if nationality.lower()=="indian" :
        print("Eligible for Aadhar Card")
    else:
        print("Not eligible for other nationality")
else:
    print("Your age is not eligible for Aadhar Card")