from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Connect to the database
def get_db_connection():
    conn = sqlite3.connect("ushering_department.db")
    conn.row_factory = sqlite3.Row
    return conn

# API Endpoints
@app.route('/members', methods=['GET'])
def get_members():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Members")
    members = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(members)

@app.route('/payments/<int:member_id>', methods=['GET'])
def get_payments(member_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Payments WHERE member_id = ?", (member_id,))
    payments = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(payments)

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

@app.route('/record-payment', methods=['POST'])
def record_payment():
    data = request.json
    member_id = data['member_id']
    month = data['month']
    amount_paid = data['amount_paid']

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Payments (member_id, month, amount_paid) VALUES (?, ?, ?)",
                   (member_id, month, amount_paid))
    conn.commit()
    conn.close()
    return jsonify({"message": "Payment recorded successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)