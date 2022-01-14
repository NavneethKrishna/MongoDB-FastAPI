from pprint import pprint
from pymongo import MongoClient
from datetime import datetime

CONNECTION_STRING = "mongodb+srv://m001-student:student@cluster0.hroxy.mongodb.net/sample_training?retryWrites=true&w=majority"

client = MongoClient(CONNECTION_STRING)
db = client['sample_training']
collection = db['trips']

"""
insert_records = {"tripduration" : 130,
                   "start station id": "SBC",
                   "start station name": "Bengaluru City Junction",
                   "end station code": "MYS",
                   "end station name": "Mysore City Junction",
                   "bikeid": 18007,
                   "usertype": "Subscriber",
                   "birth year": 1994,
                   "start station location": {"type": "Point", 
                                              "coordinates":[12.9781, 77.5695]
                                              },
                   "end station location": {"type": "Point", 
                                              "coordinates":[12.3163, 76.6454]
                                              },
                    "start time":datetime(2021, 5, 28, 11, 00, 00, 0000),
                    "stop time":datetime(2021, 5, 28, 1, 00, 00, 0000)
                    }

collection.insert_one(insert_records)
collection.insert_many(insert_records)
"""

