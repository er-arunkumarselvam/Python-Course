# Hand Cricket Game
from random import randint
# userTossValue = ' '
# toss = ["T", "H"]
# computerTossValue = toss[randint(0, 1)]
# print(type(computerTossValue))
# if userTossValue != computerTossValue:
#     userTossValue = input(print("Enter the toss (T or H) : "))
# else:
#     userTossValue = input(print("Enter the toss (T or H) : "))
#     computerTossValue = toss[randint(0, 1)]
minValue=1
maxValue=6
yourTotal = 0
yourWicket = 1
computerTotal = 0
computerWicket = 1

# select a Toss

# if userTossValue == "H":
#     selection = input(print("Select (Bat or Field) type any one option : "))
#     userSelection = selection[0].upper()+selection[1:len(selection)]
#     if userSelection == "Bat":
while yourWicket != 0:
    userScore = int(input(print("Your number is [1, 6] choose any one : ")))
    computerScore = print("Computer decide number is : ", randint(minValue, maxValue))
    if userScore != bytes(computerScore):
        yourTotal= yourTotal+ userScore
        computerScore= randint(minValue, maxValue)
        print(type(computerScore))
    else:
        yourWicket-=1
        computerScore = randint(minValue, maxValue)
else:
    print("Your First innings is completed. Next go to bowl.")
# elif userTossValue == "T":
#     print("You lose the toss. Computer choose Batting.")
#     while computerWicket != 0:
#         userScore =int(input(print("Your number is [1, 6] choose any one : ")))
#         computerScore= print("Computer deside number is : ", randint(minValue, maxValue))
#         print(type(computerScore))
#         if userScore != computerScore:
#             computerTotal = computerTotal + int(computerScore or 0)
#             computerScore = randint(minValue, maxValue)
#         else :
#             computerWicket -= 1
#             computerScore = randint(minValue, maxValue)
#     else:
#         print("Your Second innings is completed.")
#     if yourTotal > computerTotal:
#         print("You won.", yourTotal-computerTotal, " run")
#     elif yourTotal < computerTotal:
#         print("Computer won.", computerTotal-yourTotal, " run")
#     else:
#         print("The match is tie.")