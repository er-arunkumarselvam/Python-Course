# Hangman Game
name = input("Enter your name : ")
print("Welcome to the Hangman Game, ", name)
computerWord = "cricket"
guessWord = " "
life = 10
while life > 0:
    times = 0
    for letter in computerWord:
        if letter in guessWord:
            print(letter, end=" ")
        else:
            print("_ ", end=" ")
            times += 1
    if times == 0:
        print(" ,Congratulations, You Won the Game.")
        break
    print()
    guessLetter = input("Guess any one letter : ")
    guessWord += guessLetter
    if guessLetter not in computerWord:
        life -= 1
        print("Wrong, ")
        print("Try Again. ", life, " life only.")
        if life == 0:
            print("Good Effort, Try Again.")


