"""

Name: Shanie Portaal
Date: 09/13/23
Assignment: Assignment #3 SQLite3 Database
Due Date: 09/17/23
About this project:This program creates and manipulates a database using sqlite3.
Assumptions:This program assumes that the database file has the correct path.
All work below was performed by Shanie Portal

"""


import sqlite3

#Establishing connection to database.
conn = sqlite3.connect("HospitalUsers.db")

#Creating a cursor.
cur = conn.cursor()

#Delete record from table.
conn.execute('''DELETE FROM HospitalUser WHERE UserName = 'BSmith';''')

#Commit changes to database.
conn.commit()

#Print message.
print("Delete BSmith.")

#Commit changes to database.
conn.commit()

#SELECT * Statement.
cur.execute('SELECT * FROM HospitalUser;')

#Fetch all results.
results = cur.fetchall()

#Display table contents.
for row in results:
    print(row)


#Update record from table.
conn.execute('''UPDATE HospitalUser
        SET UserHasCOVID = 1
        WHERE UserName = 'AMath';''')

#Print message.
print("\nUpdate UserHasCOVID = 1 for 'AMath'.")

#Commit changes to database.
conn.commit()

#SELECT * Statement.
cur.execute('SELECT * FROM HospitalUser;')

#Fetch all results.
results = cur.fetchall()

#Display table contents.
for row in results:
    print(row)


#Print message.
print("\nA select statement that selects data from a single table.")

#SELECT Statement that selects data from a single table.
cur.execute('SELECT * FROM HospitalUser;')

#Fetch all results.
results = cur.fetchall()

#Display table contents.
for row in results:
    print(row)


#Print message.
print("\nA select statement that selects data from a single table that limits the columns returned.")

# SELECT Statement that limits the columns returned.
cur.execute('SELECT UserName, UserHasCOVID FROM HospitalUser;')

# Fetch all results.
results = cur.fetchall()

# Display table contents.
for row in results:
    print(row)

#Print message.
print("\nA select statement that selects data from a single table that limits the rows returned.")

# SELECT Statement that limits the columns returned.
cur.execute('SELECT * FROM HospitalUser WHERE UserHasCOVID = 1;')

# Fetch all results.
results = cur.fetchall()

# Display table contents.
for row in results:
    print(row)

#Print message.
print("\nA select statement that selects data from a single table that limits the columns and rows returned.")

# SELECT Statement that limits the columns returned.
cur.execute('SELECT UserName, UserHasCOVID FROM HospitalUser WHERE UserHasCOVID = 1;')

# Fetch all results.
results = cur.fetchall()

# Display table contents.
for row in results:
    print(row)

#Close database connection.
conn.close()
print("Connection closed.")