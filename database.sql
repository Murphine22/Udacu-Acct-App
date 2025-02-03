import pyodbc

# Database connection parameters
server = 'http://127.0.0.1:5000'
database = 'ushering_department.db'
username = 'Elisha Ejimofor'
password = 'Murphine22fb'

# Establish connection to the database
conn = pyodbc.connect(
    f"DRIVER={{SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password}"
)

cursor = conn.cursor()

# SQL script to create tables and insert initial data
sql_script = """
-- Create Members Table
CREATE TABLE Members (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(255) NOT NULL,
    phone_number NVARCHAR(20) NOT NULL UNIQUE
);

-- Create Payments Table
CREATE TABLE Payments (
    id INT IDENTITY(1,1) PRIMARY KEY,
    member_id INT NOT NULL,
    month NVARCHAR(20) NOT NULL,
    amount_paid DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (member_id) REFERENCES Members(id) ON DELETE CASCADE
);

-- Create Finance Table
CREATE TABLE Finance (
    id INT IDENTITY(1,1) PRIMARY KEY,
    description NVARCHAR(255) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    type NVARCHAR(20) NOT NULL CHECK(type IN ('income', 'expense', 'deduction'))
);

-- Create Admins Table
CREATE TABLE Admins (
    id INT IDENTITY(1,1) PRIMARY KEY,
    username NVARCHAR(50) NOT NULL UNIQUE,
    password NVARCHAR(255) NOT NULL
);

-- Insert Initial Admin Accounts
INSERT INTO Admins (username, password) VALUES ('elisha', '240891');
INSERT INTO Admins (username, password) VALUES ('kenneth', '1234');
INSERT INTO Admins (username, password) VALUES ('christy', '5678');
INSERT INTO Admins (username, password) VALUES ('admin4', '012345');
"""

# Execute the script
for statement in sql_script.split(';'):
    if statement.strip():  # Ignore empty statements
        cursor.execute(statement)

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()

print("Database setup completed successfully.")
