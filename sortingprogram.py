word=input("please enter any word : ")
word2=input("please enter any word : ")
if sorted(word) == sorted(word2):
    print("Two word letters are same")
else:
    print("Two word letters are not same")

mark1=int(input("Enter your mark1 : "))
mark2=int(input("Enter your mark2 : "))
mark3=int(input("Enter your mark3 : "))
if(mark1==mark2) or (mark2==mark3):
    print("All marks are same")
else:
    print("All marks are not same")