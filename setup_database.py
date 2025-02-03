import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("ushering_department.db")
cursor = conn.cursor()

# Read the SQL script
with open("database.sql", "r") as sql_file:
    sql_script = sql_file.read()

# Execute the SQL script
cursor.executescript(sql_script)

# Commit and close the connection
conn.commit()
conn.close()

print("Database and tables created successfully!")
