from datetime import date, datetime
from pymongo import MongoClient
from pprint import pprint


client = MongoClient(CONNECTIONSTRING)
mydb= client['Bus_DB'] 
information = mydb.Bus_details

# Records to insert a record to the MongoDB Database
record={
    'Vehicle_id': 145,
    'Source': 'Bengaluru',
    'Destination': 'Mangalore',
    'Date': '10/08/2022',
    'Day': 'Monday',
    'Departure_Time': '23:30',
    'Arrival_Time': '7:00',
    'Duration': '7h 30m'
}

# Insert Query
information.insert_one(record)


# Query to retrive Vehicle id
vehicle_ids = list(mydb.Bus_details.find({}, {
    "Vehicle_id": 1, "_id":False
}))

vehicle_id = []
for i in vehicle_ids:
    vehicle_id.append(i['Vehicle_id'])
print(vehicle_id)


# Query to retrieve Dates based on source and Destination
dates = list(mydb.Bus_details.find({
    "Source": 'Bengaluru','Destination': 'Mangalore',
}, {
    "Date": 1, "_id":False, 
}))
for i in dates:
    print(i)