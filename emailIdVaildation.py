#Conditions
#compulsory "@" special character
#After "@" compulsory "." special character
#not white space
email=input("Enter your Email ID : ")
emailLength=len(email)
countOfAtChar=0
countOfDot=0
countOfChar=0
countOfNumbers=0
for no in range(emailLength):
   if email[no] =="@":
       countOfAtChar+=1