# Update the database
import sqlite3
# Connection established 
connection = sqlite3.connect("//home//arun//Music//python//sqlite//Academy.db")

cursor = connection.cursor()
# update the data
cursor.execute('''UPDATE Student SET StudentName = "Kaavya" WHERE RollNo=4;''')
connection.commit()
print("update successful: ")
connection.close()