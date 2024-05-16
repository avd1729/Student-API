import os
from pymongo import MongoClient

connection_string = os.getenv("CONN_STRING")
client = MongoClient(connection_string)

if client:
    print("Connection Successful!")
else:
    print("Connection Failed!")
