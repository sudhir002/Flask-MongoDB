import os
from pymongo import MongoClient

def dbconnect():
    client = MongoClient('localhost', 27017)
    return client.filed_data