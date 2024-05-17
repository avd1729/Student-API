import os
from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps


app = Flask(__name__)

# Connect to MongoDB
connection_string = os.getenv("CONN_STRING")
client = MongoClient(connection_string)
db = client.sampledb
collection = db.students

# PUT operation to create Student information


@app.route('/students', methods=['PUT'])
def create_student():
    data = request.json

    # Generate student ID for new student
    data['_id'] = str(ObjectId())

    # Insert student data into MongoDB
    collection.insert_one(data)

    return jsonify({"message": "Student created successfully", "student_id": data['_id']}), 201


@app.route('/students/<string:student_id>', methods=['GET'])
def get_student(student_id):
    student = collection.find_one({"_id": student_id})
    if student:
        return jsonify(student), 200
    else:
        return jsonify({"message": "Student not found"}), 404


@app.route('/students', methods=['GET'])
def get_all_students():
    students = list(collection.find())
    # Convert ObjectId to string for JSON serialization
    for student in students:
        student['_id'] = str(student['_id'])
    return jsonify(students), 200


@app.route('/students/<string:student_id>', methods=['DELETE'])
def delete_student(student_id):

    delete_result = collection.delete_one({"_id": student_id})
    if delete_result.deleted_count > 0:
        return jsonify({"message": "Student deleted successfully"}), 200
    else:
        return jsonify({"message": "Student not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
