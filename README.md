# Student-API

## Overview

This Student API allows for the management of student information. It includes operations to create, retrieve, update, and delete student data, as well as a user login feature. All student data is stored in a MongoDB database in JSON format.

## Requirements

- Python 3.x
- Flask
- Flask-PyMongo
- PyMongo
- MongoDB

## Setup

### Install Dependencies

Install the required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### MongoDB
Ensure you have MongoDB installed and running on your local machine or a server.

### Configuration
Store the MongoDB connection string in a .env file

## API Endpoints

### 1. Create Student
URL: /students
Method: PUT
Description: Creates a new student record and generates a unique student ID.

### 2. Retrieve Single Student
URL: /students/<student_id>
Method: GET
Description: Retrieves information for a single student based on the student ID.

### 3. Retrieve All Students
URL: /students
Method: GET
Description: Retrieves information for all students.

### 4. Update Student
URL: /students/<student_id>
Method: PUT
Description: Updates information for a student based on the student ID.

### 5. Delete Student
URL: /students/<student_id>
Method: DELETE
Description: Deletes a student record based on the student ID.

### 6. User Login
URL: /login
Method: POST
Description: Verifies user ID and password (this service uses hard-coded values for demonstration purposes).

## Running the Application
Ensure MongoDB is running.
Run the Flask application:

```bash
python app.py
```
The API will be available at http://127.0.0.1:5000.
