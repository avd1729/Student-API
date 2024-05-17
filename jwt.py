import os
import json
from flask import Flask, jsonify, request, make_response
import jwt
from functools import wraps
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")
connection_string = os.getenv("CONN_STRING")
client = MongoClient(connection_string)
db = client.sampledb
collection = db.students


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')
        if not token:
            return jsonify({'error': 'Authorization token is missing'}), 401
        try:
            data = jwt.decode(
                token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user_id = data['user_id']
        except jwt.DecodeError:
            return jsonify({'error': 'Authorization token is invalid'}), 401
        return f(current_user_id, *args, **kwargs)
    return decorated


@app.route('/students', methods=['PUT'])
@token_required
def create_student(current_user_id):
    data = request.json
    data['_id'] = str(ObjectId())
    collection.insert_one(data)
    return jsonify({"message": "Student created successfully", "student_id": data['_id']}), 201


@app.route('/students/<string:student_id>', methods=['GET'])
@token_required
def get_student(current_user_id, student_id):
    student = collection.find_one({"_id": student_id})
    if student:
        student['_id'] = str(student['_id'])  # Convert ObjectId to string
        return jsonify(student), 200
    else:
        return jsonify({"message": "Student not found"}), 404


@app.route('/students', methods=['GET'])
@token_required
def get_all_students(current_user_id):
    students = list(collection.find())
    for student in students:
        student['_id'] = str(student['_id'])  # Convert ObjectId to string
    return jsonify(students), 200


@app.route('/students/<string:student_id>', methods=['DELETE'])
@token_required
def delete_student(current_user_id, student_id):
    delete_result = collection.delete_one({"_id": student_id})
    if delete_result.deleted_count > 0:
        return jsonify({"message": "Student deleted successfully"}), 200
    else:
        return jsonify({"message": "Student not found"}), 404


@app.route('/students/<string:student_id>', methods=['PUT'])
@token_required
def update_student(current_user_id, student_id):
    try:
        student_id = ObjectId(student_id)  # Convert string ID to ObjectId
    except:
        return jsonify({"message": "Invalid student ID format"}), 400

    data = request.json
    if not data:
        return jsonify({"message": "No data provided"}), 400

    update_result = collection.update_one({"_id": student_id}, {"$set": data})
    if update_result.modified_count > 0:
        return jsonify({"message": "Student updated successfully"}), 200
    else:
        return jsonify({"message": "Student not found"}), 404


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    with open('users.json', 'r') as f:
        users = json.load(f)
    for user in users:
        if user['username'] == data.get('username') and user['password'] == data.get('password'):
            token = jwt.encode(
                {'user_id': user['id']}, app.config['SECRET_KEY'], algorithm="HS256")
            response = make_response(
                jsonify({"message": "Login successful"}), 200)
            response.set_cookie('token', token)
            return response
    return jsonify({"message": "Invalid credentials"}), 401


if __name__ == '__main__':
    app.run(debug=True)
