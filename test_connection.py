import sqlite3

# Connect to database
conn = sqlite3.connect("ushering_department.db")
cursor = conn.cursor()

# Fetch all admin users
cursor.execute("SELECT * FROM Admins")
admins = cursor.fetchall()

# Print results
for admin in admins:
    print(admin)

conn.close()
