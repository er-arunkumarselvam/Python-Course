# create, update and delete database
import sqlite3
# Connection established 
connection = sqlite3.connect(r"/home/arun/Music/python/sqlite/Academy.db")

cursor = connection.cursor()
cursor.execute("""DROP TABLE STUDENT;""")
# execute sql query in the database using execute()
cursor.execute("""CREATE TABLE Student(
        RollNo INTEGER PRIMARY KEY,
        StudentName VARCHAR(25),
        Gender CHAR(1),
        DOB DATE,
        Percentage DECIMAL(5,2)
        );""")
cursor.execute("""INSERT INTO Student(RollNo,StudentName,Gender,DOB,Percentage)
               VALUES(NULL, "Arunkumar",'M','1998-12-05', 75.64);""")

#list of students data
studentsList =[("Nandhini", "F","2001-06-15", 80.7),
               ("Prasanna", "M","2002-05-04", 76.1),
               ("Shalini", "F","2002-12-12", 60.5),
               ("Pandiyan", "M","1999-11-30", 72.7)]

for student in studentsList:
    studentFormat ="""INSERT INTO student(RollNo,StudentName,Gender,DOB,Percentage)
                VALUES(NULL, "{name}","{gender}","{dob}","{percentage}");"""
    
    studentsData = studentFormat.format(name=student[0],gender=student[1],dob=student[2],percentage=student[3])
    cursor.execute(studentsData)
# important commands it like a similar for ctrl+s (save data)
connection.commit()
connection.close()



    



