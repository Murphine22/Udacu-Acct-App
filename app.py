from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Connect to the database
def get_db_connection():
    conn = sqlite3.connect("ushering_department.db")
    conn.row_factory = sqlite3.Row
    return conn

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Admin Login API
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Admins WHERE username = ? AND password = ?", (username, password))
    admin = cursor.fetchone()
    conn.close()

    if admin:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# Add Member API
@app.route('/add-member', methods=['POST'])
def add_member():
    data = request.json
    name = data['name']
    phone_number = data['phone_number']

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO Members (name, phone_number) VALUES (?, ?)", (name, phone_number))
        conn.commit()
        conn.close()
        return jsonify({"message": "Member added successfully"}), 201
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({"error": "Phone number already exists"}), 400

if __name__ == '__main__':
    app.run(debug=True)