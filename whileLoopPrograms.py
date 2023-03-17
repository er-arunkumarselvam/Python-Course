#Print vowels only print
word=input("enter any word : ")
length=len(word)
no=0
count=0
while no<length:
    #if word[no]=='a' or word[no]== 'e' or word[no]== 'i' or word[no]=='o'or word[no]== 'u':
    if word[no] in (['a','e','i','o','u','A','E','I','O','U']):
        print(word[no])
        count+=1
    no+=1
print("No.of Vowels is present : ",count)
print("The number of letters is " , no)

no=1
while no<=5:
 print(no)
 no+=1
 # break
else:
  print('hi')
