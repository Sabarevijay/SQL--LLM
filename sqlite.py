# import sqlite3

# ## Connectt to SQlite
# connection=sqlite3.connect("student.db")

# # Create a cursor object to insert record,create table

# cursor=connection.cursor()
# cursor.execute("DROP TABLE IF EXISTS STUDENT")

# ## create the table

# table_info = """
# CREATE TABLE STUDENT(
#     NAME VARCHAR(25),
#     SUBJECT VARCHAR(25),
#     MARKS INT,
#     REG_NO VARCHAR(25),
#     EMAIL_ID VARCHAR(25),
#     CLASS VARCHAR(25)
# );
# """
# cursor.execute(table_info)

# ## Insert Some more records

# cursor.execute('''Insert Into STUDENT values('ISHWARYA','HUMAN VALUES AND ETHICS',36,'7376232AD157','ishwarya.ad23@bitsathy.ac.in','AIDS')''')
# cursor.execute('''Insert Into STUDENT values('JEYALAKSHMI','COMPUTER ARCHITECTURE',35,'7376232AD165','jeyalakshmi.ad23@bitsathy.ac.in','AIDS')''')
# cursor.execute('''Insert Into STUDENT values('MONISHADHITH','COMPUTER ARCHITECTURE',29,'7376231CS229','monishadhith.cs23@bitsathy.ac.in','CSE')''')
# cursor.execute('''Insert Into STUDENT values('MOHAMMED','HUMAN VALUES AND ETHICS',29,'7376231EI126','mohammeda.ei23@bitsathy.ac.in','EIE')''')
# cursor.execute('''Insert Into STUDENT values('MADUMITHA','COMPUTER ARCHITECTURE',20,'7376232AD188','madumitha.ad23@bitsathy.ac.in','AIDS')''')

# ## Disspaly ALl the records

# print("The inserted records are")
# data=cursor.execute('''Select * from STUDENT''')
# for row in data:
#     print(row)

# ## Commit your changes int he databse
# connection.commit()
# connection.close()



import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("student.db")

# Create a cursor object
cursor = connection.cursor()

# Query to retrieve data from the existing 'my_table'
query = "SELECT * FROM my_table"

# Execute the query
cursor.execute(query)

# Fetch all records
records = cursor.fetchall()

# Display the records
print("The existing records in my_table are:")
for row in records:
    print(row)

# Close the database connection
connection.close()




