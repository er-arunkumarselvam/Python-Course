#If Else Statement
"""system =5
user=int(input("Guess the Number : "))
if(system==user):
    print("Your Guess is Correct.")
elif(system>user):
    print("Your Guess is Lower.")
elif(system<user):
    print("Your Guess is Higher.")"""

#While Loop
system =5
match_not_found=True

while match_not_found== True:
    user = int(input("Enter a number between 1 to 10 : "))
    if (system == user):
        print("Congrats, Your Guess is Correct.")
        #match_not_found = False
        break
    elif (system > user):
        print("Your Guess is Lower.")
    elif (system < user):
        print("Your Guess is Higher.")
