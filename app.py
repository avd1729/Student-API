import os
from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId

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


if __name__ == '__main__':
    app.run(debug=True)
