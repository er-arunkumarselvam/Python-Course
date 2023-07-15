# Delete the database
import sqlite3
# Connection established 
connection = sqlite3.connect("//home//arun//Music//python//sqlite//Academy.db")

cursor = connection.cursor()
# delete the data
cursor.execute("DELETE from Student where StudentName='Kaavya'");
connection.commit()
print("Total no.of rows deleted: ",connection.total_changes)
connection.close()