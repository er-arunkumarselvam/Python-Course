# Stone Paper Scissor Game
from random import randint

# creating play options using numbers
options = ["Stone", "Paper", "Scissor"]  # 0, 1, 2

computer = options[randint(0, 2)]

repeat = 'Y'
while repeat == 'Y':
    play = input("Type your choice [ Stone, Paper, Scissor ] any one : ")
    player = play[0].upper() + play[1:len(play)]
    print (player)
    print(computer)
    if player == computer:
        print("Game is Tie!")
    elif player == "Stone":
        if computer == "Paper":
            print("Computer won!", computer, "- You lose!", player)
        else:
            print("You won!", player, "- Computer lose!", computer)
    elif player == "Paper":
        if computer == "Scissor":
            print("Computer won!", computer, "- You lose!", player)
        else:
            print("You won!", player, "- Computer lose!", computer)
    elif player == "Scissor":
        if computer == "Stone":
            print("Computer won!", computer, "- You lose!", player)
        else:
            print("You won!", player, "- Computer lose!", computer)


    else:
        print("Please Check Your Spelling.")
    y_or_n = input("Press 'Y' continue another game. otherwise not. ")
    repeat = y_or_n.upper()
    if repeat != 'Y':
        print("Thank You. Visit Again.")
    computer = options[randint(0, 2)]