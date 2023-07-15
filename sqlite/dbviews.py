# Read the database
import sqlite3
# Connection established 
connection = sqlite3.connect(r"/home/arun/Music/python/sqlite/Academy.db")

cursor = connection.cursor()
cursor.execute("SELECT * FROM Student") # * - Every column values in the table
# fetchone()
onedisplayData = cursor.fetchone()
for data1 in onedisplayData:
    print(data1)
# fetchone() and while
result = cursor.fetchone()
while result is not None:
    print(result)
    result = cursor.fetchone()
# fetchall()
displayData = cursor.fetchall()
for data in displayData:
    print(data)
# fetchmany()
resultData = cursor.fetchmany(2) # 2 denotes 1,2 rows data
for datas in resultData:
    print(datas)
# Particalar Columns only read
cursor.execute("SELECT DISTINCT(StudentName) FROM Student")
particularData = cursor.fetchmany(2)
for part in particularData:
    print(part)
# COUNT THE DATA
cursor.execute("SELECT count(*) FROM Student") # number rows data add in the table
results=cursor.fetchall()
print(results)
# not equalant <>
cursor.execute("SELECT RollNo,StudentName from Student where gender<>'M' and gender<>'F' ")
results=cursor.fetchall()
print(results, sep='\n')


