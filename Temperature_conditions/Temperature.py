from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient 
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from bson import ObjectId
import logging

load_dotenv()

mongo_url = os.environ.get("MONGO_URL")
if not mongo_url:
    raise ValueError("mongo_url not set")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info(f"SUCCESSFULLY CONNECTED TO MONGO_URL") 

client = AsyncIOMotorClient(mongo_url)
db = client.get_database("weather")
Weather_Collection = db.get_collection("forecast")



#create an instance of a fast api application
app = FastAPI()

class WeatherData(BaseModel):
        temperature : str
        # humidity : str
        response_description : str


#create an instance of a fast api application


#define a route at the route web address
@app.get("/Temperature_Information",
    response_description="List current temperature information",
    response_model=WeatherData
)

async def get_temp():
    # creating a connection with mongodb
    # client = AsyncIOMotorClient(os.env["MONGO_URL"])
 
    # #interaction with the weather database
    # db = client.get_database("weather")
    # Weather_Collection = db.get_collection("forecast")
    latest_weather_data = await Weather_Collection.find_one({}, sort=[("_id", -1)])
    if latest_weather_data:
        return WeatherData(
            temperature=latest_weather_data.get("temperature", "N/A"),
            # humidity=latest_weather_data.get("humidity", "N/A"),
            response_description=latest_weather_data.get("response_description", "List current temperature Information")
           ) 
    else:
        raise HTTPException(status_code=404, detail="Weather information not found")


