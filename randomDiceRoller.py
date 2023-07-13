# Random Dice Roller Game
# Module - group of functions
# Library - number of modules
# from, import - python reserved keyword
# random - Module
# randint - function (2 argument passing) - integer - random integer

from random import randint
# from random (import only a module)
minValue = 1
maxValue = 6
print("Random Dice Roller Game")
playAgain = True
while playAgain:
    print("Dice Value now : ", randint(minValue, maxValue))# random.randint(minValue, maxValue) using dot '.' split the module and functions
    print(type(randint(minValue, maxValue)))
    nextTime = input("Press 'y' if you want to roll on dice again : ")
    if nextTime.lower() == 'y' or nextTime.lower() == 'yes':
        playAgain = True
    else:
        playAgain = False
        print("Thank you, Visit Again.")
