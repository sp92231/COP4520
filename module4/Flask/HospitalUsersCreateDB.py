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

# Establishing connection to database.
conn = sqlite3.connect('HospitalUsers.db')
# Creating a cursor.
cur = conn.cursor()

# Dropping table.
conn.execute('''Drop table HospitalUser''')
print("HospitalUser Table Dropped.")

# Commit changes to database.
conn.commit()

# Creating table HospitalUser.
cur.execute('''CREATE TABLE HospitalUser(
Name TEXT PRIMARY KEY NOT NULL,
Age INT NOT NULL,
PhoneNumber TEXT NOT NULL,
COVID INTEGER NOT NULL,
SecurityLevel INTEGER NOT NULL,
Password TEXT NOT NULL);
''')
# Print message.
print("HospitalUser Table Created.")

# Commit changes to database.
conn.commit()

# Insert data into table.
cur.executescript('''INSERT INTO HospitalUser VALUES
                ('PDiana', '34', '123-675-7645', 0, 1, 'test123');

                INSERT INTO HospitalUser VALUES
                ('TJones', '68', '895-345-6523', 1, 2, 'test123');

                INSERT INTO HospitalUser VALUES
                ('AMath', '29', '428-197-3967', 0, 3, 'test123');

                INSERT INTO HospitalUser VALUES
                ('BSmith', '37', '239-567-3498', 1, 2, 'test123');

                ''')

# Commit changes to database.
conn.commit()

# SELECT * Statement.
cur.execute('SELECT * FROM HospitalUser;')

# Fetch all results.
results = cur.fetchall()

# Display table contents.
for row in results:
    print(row)

# Close database connection.
conn.close()
print("Connection closed.")




