# Get the value of total number students
# Collect the Name, Age, Percentage with all students
# Store the 3 list in single list
# Above 75% to display the Name and Age

# two sentence or string using without concatination operator is possible in python
studentsCount = int(input("Hi Sir/Madam" "Enter the No. of Students in the class : "))
studentsDetails = []
for collectDetails in range(studentsCount):
    name, age, percentage = input("Enter your name, age and percentage with space :  ").split()
    # print("Enter your Details : ",name, age, percentage)
    studentsDetails.append(name)
    studentsDetails.append(age)
    studentsDetails.append(percentage)
#print(studentsDetails)
print ("Qualified Students (Above 75% only )")
count=1
for data in studentsDetails:
    if count % 3 == 0:
        if int(data) > 75:
            print("Name : ",studentsDetails[count-3])
            print("Age : ",studentsDetails[count-2])
    count += 1
print()
