from fastapi import FastAPI
from pymongo import MongoClient
from bson import json_util
import json
from pydantic import BaseModel
from datetime import date, datetime
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

CONNECTION_STRING = "mongodb+srv://m001-student:student@cluster0.hroxy.mongodb.net/sample_training?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)
db = client['sample_training']
collection = db['trips']

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

class Trip(BaseModel):
    tripduration : int
    start_station_id: str
    start_station_name: str
    end_station_code: str
    end_station_name: str
    usertype: str
    birth_year: int
    start_station_location: list()
    end_station_location: list()
    start_time: date
    stop_time:date

@app.post("/insert/")
async def insert(trip: Trip):
    records = trip.dict()
    collection.insert_one(parse_json(records))
    return records