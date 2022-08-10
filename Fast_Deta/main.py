from fastapi import FastAPI
from pymongo import MongoClient
from bson import json_util
import json
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

client = MongoClient(CONNECTIONSTRING)
mydb= client['Bus_DB'] 
information = mydb.Bus_details

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def parse_json(data):
    return json.loads(json_util.dumps(data))

class BusDetails(BaseModel):
    vehicle_id: int
    Source:str
    Destination: str
    Date: str
    Day : str
    Departure_Time: str
    Arrival_Time: str
    Duration: str


@app.post("/insert/")
async def insert(bus_details: BusDetails):
    record= bus_details.dict()
    information.insert_one(parse_json(record))
    return record

@app.get("/")   
async def get_all_vehicles():
    vehicle_ids = list(mydb.Bus_details.find({}, {
        "Vehicle_id": 1, "_id":False
    }))

    vehicle_id = []
    for i in vehicle_ids:
        vehicle_id.append(i['Vehicle_id'])
    return vehicle_id

@app.get("/Source/{Source}/Destination/{Destination}/get_bus_dates/")   
async def get_bus_dates(Source, Destination):
    date = []
    dates = list(mydb.Bus_details.find({"Source": Source,'Destination': 'Mangalore'}, {"Date": 1, "_id":False}))
    for i in dates:
        date.append(i['Date'])
    return date