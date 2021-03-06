from pymongo import MongoClient
import os

password=os.getenv('mongo_password')
client = MongoClient(f'mongodb+srv://user1:{password}@cluster0-bf7gi.mongodb.net/test?retryWrites=true&w=majority')
db = client['InteractivityChallenge']
collection = db['individualUser']

def find():
    record_list = []
    records = collection.find({}).sort("timestamp") #sorting to be fixed
    for record in records:
        record_list.append(record)
    # print(record_list)
    return record_list