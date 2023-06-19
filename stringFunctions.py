# Some String Functions
name = "arunkumar"
print(name.capitalize())  # Convert the first character of a string to uppercase
name = "ARUN"
print(name.casefold())  # Change into small letters
name = "Credit Card Validator"
print(name.center(30, "*"))  # 30 width and indicate *  ==> ****Credit Card Validator*****
sentence = "What is your name?"
word = "is"
print(sentence.count(word))  # Returns the number of occurrences of a substring in the string.
print(sentence.endswith("name?"))  # Returns “True” if a string ends with the given suffix
sentence="My \tname \tis \tArunkumar "
print(sentence.expandtabs(12)) # Specifies the amount of space to be substituted with the “\t” symbol in the string, default - 8, no float value used
print(sentence.find("What"))  # Returns the lowest index of the substring if it is found
txt = "I have {an:.2f} Rupees!"
print(txt.format(an=4))  # Formats the string for printing it to console
name = "vijay"
print(name.upper())  # Converts all lowercase characters in a string into uppercase
name = "KRISHNAKUMAR"
print(name.lower())  # Converts all uppercase characters in a string into lowercase
title = "introduction"
print(title.title())  # Convert string to title case
name = "String functions"
print(name.swapcase())  # Swap the cases of all characters in a string
string = 'random'
print(string.index('and'))  # Returns the position of the first occurrence of a substring in a string
string = "Hi"
print(string.isidentifier())  # Check whether a string is a valid identifier or not
