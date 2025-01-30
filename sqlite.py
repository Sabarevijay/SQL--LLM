import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()
cursor.execute("DROP TABLE IF EXISTS STUDENT")

## create the table

table_info = """
CREATE TABLE STUDENT(
    NAME VARCHAR(25),
    SUBJECT VARCHAR(25),
    MARKS INT,
    REG_NO VARCHAR(25),
    EMAIL_ID VARCHAR(25),
    CLASS VARCHAR(25)
);
"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into STUDENT values('ISHWARYA','HUMAN VALUES AND ETHICS',36,'7376232AD157','ishwarya.ad23@bitsathy.ac.in','AIDS')''')
cursor.execute('''Insert Into STUDENT values('JEYALAKSHMI','COMPUTER ARCHITECTURE',35,'7376232AD165','jeyalakshmi.ad23@bitsathy.ac.in','AIDS')''')
cursor.execute('''Insert Into STUDENT values('MONISHADHITH','COMPUTER ARCHITECTURE',29,'7376231CS229','monishadhith.cs23@bitsathy.ac.in','CSE')''')
cursor.execute('''Insert Into STUDENT values('MOHAMMED','HUMAN VALUES AND ETHICS',29,'7376231EI126','mohammeda.ei23@bitsathy.ac.in','EIE')''')
cursor.execute('''Insert Into STUDENT values('MADUMITHA','COMPUTER ARCHITECTURE',20,'7376232AD188','madumitha.ad23@bitsathy.ac.in','AIDS')''')

## Disspaly ALl the records

print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()





# import sqlite3

# # Connect to SQLite
# connection = sqlite3.connect("student.db")

# # Create a cursor object
# cursor = connection.cursor()

# # Create the table if it doesn't exist
# table_info = """
# CREATE TABLE IF NOT EXISTS STUDENT(
#     NAME VARCHAR(25),
#     CLASS VARCHAR(25),
#     SECTION VARCHAR(25),
#     MARKS INT
# );
# """
# cursor.execute(table_info)

# # Insert records into the table
# cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
# cursor.execute('''Insert Into STUDENT values('Sudhanshu','Data Science','B',100)''')
# cursor.execute('''Insert Into STUDENT values('Darius','Data Science','A',86)''')
# cursor.execute('''Insert Into STUDENT values('Vikash','DEVOPS','A',50)''')
# cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')
# connection.commit()

# # Execute the query to fetch names where MARKS = 90
# query = "SELECT  FROM STUDENT WHERE MARKS = 90"
# cursor.execute(query)

# # Fetch and display the results
# results = cursor.fetchall()
# print("Names of students where MARKS = 90:")
# if results:
#     for row in results:
#         print(row[0])  # Print only the NAME column
# else:
#     print("No records found.")

# # Close the connection
# connection.close()

