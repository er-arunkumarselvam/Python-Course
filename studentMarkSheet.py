# Student Mark Sheet
studentsCount = int(input("Enter the no. of students : "))
report = {}  # dict
subjects = ('Tamil', 'English', 'Maths', 'Science', 'SocialScience')  #tuple
for student in range(studentsCount):
    name = input("Enter the name of the student %d : "% (student + 1))
    marks = []
    for subject in subjects:
        mark = int(input("Enter your mark for %s : " % subject))
        marks.append(mark)
        report[name] = marks
    for name, marks in report.items():
        total = sum(marks)
        print("%s 's total marks : %d  " % (name, total))
        if marks < 120:
            print("%s Failed : ("% name)
        else:
            print("%s Passed : )" % name)