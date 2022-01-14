import collections
from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://m001-student:student@cluster0.hroxy.mongodb.net/sample_training?retryWrites=true&w=majority"

client = MongoClient(CONNECTION_STRING)
db = client['sample_training']
collection = db['trips']

print(len(list(collection.find({ }, {"start station id": 1, "_id":False}).distinct())))