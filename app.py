import os
from flask import Flask, jsonify, request, send_from_directory
from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps

app = Flask(__name__)

# Connect to MongoDB
connection_string = ""
client = MongoClient(connection_string)
db = client.sampledb
collection = db.students

# Serve static files (HTML, JS, CSS)


@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')


@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

# PUT operation to create Student information


@app.route('/students', methods=['PUT'])
def create_student():
    data = request.json
    if not data:
        return jsonify({"error": "Invalid data"}), 400

    try:
        data['_id'] = ObjectId()
        collection.insert_one(data)
        return jsonify({"message": "Student created successfully", "student_id": str(data['_id'])}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET operation to get a single Student information


@app.route('/students/<string:student_id>', methods=['GET'])
def get_student(student_id):
    student = collection.find_one({"_id": ObjectId(student_id)})
    if student:
        json_data = dumps(student)
        return json_data, 200
    else:
        return jsonify({"message": "Student not found"}), 404

# GET operation to get all student information


@app.route('/students', methods=['GET'])
def get_all_students():
    students = list(collection.find())
    for student in students:
        student['_id'] = str(student['_id'])
    json_data = dumps(students)
    return json_data, 200

# DELETE operation to delete a single Student


@app.route('/students/<string:student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        student_id = ObjectId(student_id)
    except:
        return jsonify({"message": "Invalid student ID format"}), 400

    delete_result = collection.delete_one({"_id": student_id})
    if delete_result.deleted_count > 0:
        return jsonify({"message": "Student deleted successfully"}), 200
    else:
        return jsonify({"message": "Student not found"}), 404

# PUT operation to update a single Student information


@app.route('/students/<string:student_id>', methods=['PUT'])
def update_student(student_id):
    try:
        student_id = ObjectId(student_id)
    except:
        return jsonify({"message": "Invalid student ID format"}), 400

    data = request.get_json()
    if not data:
        return jsonify({"message": "No data provided"}), 400

    update_result = collection.update_one({"_id": student_id}, {"$set": data})
    if update_result.modified_count > 0:
        return jsonify({"message": "Student updated successfully"}), 200
    else:
        return jsonify({"message": "Student not found"}), 404

# POST operation for login


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if data.get('username') == 'admin' and data.get('password') == 'admin':
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401


if __name__ == '__main__':
    app.run(debug=True)
