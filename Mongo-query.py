from datetime import datetime
from pymongo import MongoClient
from pprint import pprint


client = MongoClient("mongodb+srv://Lavy:bus@bus.u3kvn.mongodb.net/?retryWrites=true&w=majority")
mydb= client['Bus_DB'] 
information = mydb.Bus_details


# information.update_one({"vehicle_id": 1, "date_field": "10-01-2022"}, {"$set":{'live':0}})
# information.delete_many({ })

record={
    'Vehicle_id': 125,
    'Source': 'Bengaluru',
    'Destination': 'Mysore',
    'Date': datetime(2022, 8, 4),
    'Day': 'Monday',
    'Departure_Time': datetime(2022, 8, 4, 1, 30, 00),
    'Arrival_Time': datetime(2022, 8, 4, 4, 30, 00),
    'Duration': '3h 00m'
}

information.insert_one(record)