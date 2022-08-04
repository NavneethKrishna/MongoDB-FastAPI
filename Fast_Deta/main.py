from fastapi import FastAPI
from pymongo import MongoClient
from bson import json_util
import json
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

client = MongoClient(ConnectionString)
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
