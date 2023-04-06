#Conditions
#Atleast Min. 8 Character to Max. 20 Character
#Atleast 1 Capital Letter
#Atleast 1 Small Letter
#Atleast 1 Numeric Letter
#Atleast 1 Special Character

password=input("Enter your password (min:8) : ")
length=len(password)
countUpperCase=0
countLowerCase=0
countNumber=0
countSpecial=0
passLength=False
if(len(password)>=8):
    passLength=True
else:
    print("Atleast Mininum 8 Character")
    password = input("Enter your password (min:8) : ")
for no in range(length):
        if(password[no]>='a'and password[no]<='z'):
            countLowerCase=countLowerCase+1
        elif (password[no]>='A'and password[no]<='Z'):
            countUpperCase=countUpperCase+1
        elif (password[no]>='0'and password[no]<='9'):
            countNumber=countNumber+1
        elif (password[no]or['#','@','$','.','&','!','%']):
            countSpecial=countSpecial+1
if(countUpperCase!=0 and countLowerCase!=0 and countNumber!=0 and countSpecial!=0):
    print("Password Successfully.")
else:
    if(countUpperCase==0):
        print("Enter atleast 1 capital letter.")
    if(countLowerCase==0):
        print("Enter atleast 1 small letter")
    if(countNumber == 0):
        print("Enter atleast 1 number")
    if(countSpecial== 0):
        print("Enter atleast 1 special character")