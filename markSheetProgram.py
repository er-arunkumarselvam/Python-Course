#Mark Sheet Program
min_no_of_subject=1
no_of_subjects=int(input("Enter the No.of Subjects : "))
total=0
while min_no_of_subject<=no_of_subjects:
    subject=int(input("Please, Enter your mark : "))
    total+=subject
    min_no_of_subject+=1
print("Your Total Mark is ", total)
print("Your Percentage is ",total/no_of_subjects)