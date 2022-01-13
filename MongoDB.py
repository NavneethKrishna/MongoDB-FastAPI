from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://<username>:<password>@cluster0.hroxy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = MongoClient(CONNECTION_STRING)
db = client['trips']

print(list(db.sample_training.find({"birth year" : 1969})) )
