from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
import os
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from pydantic import BaseModel, Field
import logging


load_dotenv()

# mongo_url = os.environ.get("MONGO_URL")
mongo_url = os.getenv("MONGO_URL")
if not mongo_url:
    raise ValueError("mongo_url is not set")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)    
logger.info(f"SUCCESSFULLY CONNECTED TO MONGO_URL")

client = AsyncIOMotorClient(mongo_url)
db = client.get_database("weather")
Weather_Collection = db.get_collection("forecast")


#Creating a fast api instance 
app = FastAPI()

class WeatherData(BaseModel):
    humidity : str
    response_description : str
    
#defines the route to get the information for the humidity
@app.get("/Humidity_Information",
        response_description="Display the current humidity", 
        response_model=WeatherData      
)

async def get_humid():
    latest_weather_data = await Weather_Collection.find_one({}, sort=[("_id", -1)])
    if latest_weather_data:
        return WeatherData(
            humidity=latest_weather_data.get("humidity", "N/A"),
            response_description=latest_weather_data.get("response_description", "This displays the current humidity")
        )
        
    else: 
        raise HTTPException(
            status_code=404, #An error code that indicates that the requested resource could not be found and it is more of client error
            detail="humidity information not found"
        )  