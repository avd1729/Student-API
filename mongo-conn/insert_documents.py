from datetime import datetime
import os
from pymongo import MongoClient

connection_string = ""
client = MongoClient(connection_string)

db = client.sampledb
collection = db.students


sample_data = [
    {
        "roll number": 1,
        "name": "John Doe",
        "dob": datetime(2005, 5, 15),
        "class": "10",
        "section": "A",
        "classteacher": "Mr. Smith",
        "active": True,
        "fee": "paid"
    },
    {
        "roll number": 2,
        "name": "Alice Smith",
        "dob": datetime(2006, 8, 25),
        "class": "9",
        "section": "B",
        "classteacher": "Ms. Johnson",
        "active": True,
        "fee": "paid"
    },
    {
        "roll number": 3,
        "name": "Sophie Turner",
        "dob": datetime(2006, 9, 2),
        "class": "10",
        "section": "A",
        "classteacher": "Mr. Smith",
        "active": True,
        "fee": "paid"
    },
    {
        "roll number": 4,
        "name": "Daniel White",
        "dob": datetime(2007, 4, 15),
        "class": "9",
        "section": "B",
        "classteacher": "Ms. Johnson",
        "active": True,
        "fee": "unpaid"
    },
    {
        "roll number": 5,
        "name": "Mia Thompson",
        "dob": datetime(2005, 11, 23),
        "class": "8",
        "section": "C",
        "classteacher": "Mrs. Anderson",
        "active": True,
        "fee": "unpaid"
    },
    {
        "roll number": 6,
        "name": "Ethan Harris",
        "dob": datetime(2006, 6, 8),
        "class": "11",
        "section": "A",
        "classteacher": "Mr. Davis",
        "active": True,
        "fee": "paid"
    },
    {
        "roll number": 7,
        "name": "Sophia Clark",
        "dob": datetime(2007, 3, 20),
        "class": "10",
        "section": "B",
        "classteacher": "Ms. Martinez",
        "active": True,
        "fee": "unpaid"
    },
    {
        "roll number": 8,
        "name": "Jacob Lee",
        "dob": datetime(2005, 8, 12),
        "class": "9",
        "section": "A",
        "classteacher": "Mrs. Clark",
        "active": True,
        "fee": "paid"
    },
    {
        "roll number": 9,
        "name": "Ava Rodriguez",
        "dob": datetime(2006, 1, 28),
        "class": "8",
        "section": "B",
        "classteacher": "Mr. Hernandez",
        "active": True,
        "fee": "unpaid"
    },
    {
        "roll number": 10,
        "name": "Noah Diaz",
        "dob": datetime(2007, 7, 5),
        "class": "11",
        "section": "C",
        "classteacher": "Mrs. Lopez",
        "active": True,
        "fee": "unpaid"
    }
]

collection.insert_many(sample_data)

print("Sample data inserted successfully.")
