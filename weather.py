
# import requests
# from pymongo import MongoClient
# import os
# import boto3
# import json

# mongo_url = os.getenv("MONGO_URL")
# secretId ="Mongo_db_cred"
# region_name = "us-east-1"
 
# def get_mongo_url():
#    client = boto3.client("secretsmanager", region_name=region_name)
#    response = json.loads(client.get_secret_value(SecretId=secretId)["SecretString"])
#    return(response)
#    print(response)
   
# get_mongo_url()
# mongo_client = MongoClient(get_mongo_url())
# db = mongo_client.weather

# # # MONGO_URI = os.getenv("MONGO_URI")
# # # API_KEY = os.getenv("OPENWEATHER_API_KEY")


# # city = "Lagos"
 
  
# #  mongoDB = MongoClient(MONGO_URI)
# #  db = mongoDB.weather
# #  collection = db.weather_data
 
# #  API_URL = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
 
# #  response = requests.get(API_URL)
# # #  if  response.status_code == "200":
# # #      print("API CALL WAS SUCCESSFUL") 

# #  data = response.json()

# #     # for forecast in data["list"]:
# #  temp_document = {
# #                 "city" : data["city"]["name"],
# #                 "country" : data["city"]["country"],
# #                 "Temperature" :  data["list"][0]["main"]["temp"],
# #                 "Humidity" : data["list"][0]["main"]["humidity"],
# #                 "wind speed trend" : data["list"][0]["wind"]["speed"],
# #                 "datetime": data["list"][0]["dt_txt"]
                
# #  }
 
# #  collection.insertOne(temp_document)
# #  print(f"Data has been inserted :{temp_document}")

#  from pymongo import MongoClient
# import requests
# import os
# import boto3
# import json
# #All necessary variables being listed and some were not hardcoded as they are sensitive information that are to be stored as an environment variable

# secretId = os.getenv("SECRET_ID")
# region_name = "us-east-1"
# API_KEY = os.getenv("API_KEY")
# city = "Lagos"
# # API_URL = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"

# def get_mongo_url():
#     try:
#         client = boto3.client("secretsmanager", region_name=region_name)
#         response = client.get_secret_value(SecretId=secretId)
#         secret = json.loads(response["SecretString"])
#         return secret["url"]

#     except Exception as e:
#         print(f"Error fetching secrets: {e}")
#         return None

# def lambda_handler(event, context):
#     try:
#         action = event.get("action")
#         city = event.get("city")
#         if action != "fetch_weather":
#             return{
#                 "statusCode" : 400,
#                 "body" : json.dumps({
#                     "message" : "Invalid action. Supported action: fetch_weather"
#                 })
#             }

#         API_URL = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"

#         mongo_url = get_mongo_url()
#         mongo_client = MongoClient(mongo_url)
#         print("Connected to MongoDB successfully")

#         db = mongo_client.weather
#         print("Talked to weather database")

#         collections = db.list_collection_names() #lists all collections in the database
#         response = requests.get(API_URL) #communication with the open weather site to fetch the information bassed on the city
#         data = response.json() #This converts a JSON-formatted response from an HTTP request into  a python object
#         print(data)

# #Getting the necessary information needed from the open weather api platfor
#         Weather_information = {
#             "city": data["city"]["name"],
#             "country" : data["city"]["country"],
#             "temperature" : data["list"][0]["main"]["temp"],
#             "humidity" : data["list"][0]["main"]["humidity"],
#             "wind_speed_trend" : data["list"][0]["wind"]["speed"],
#             "datetime" : data["list"][0]["dt_txt"]
#             }
#         collection_name = "forecast"
#         if collection_name not in db.list.collection_names():
#             db.create_collection(collection_name)
#             print(f"Collection '{collection_name}' created successfully")

#         db.forecast.insert_one(Weather_information)
#         print(f"Weather information successfully put into mongo db: {Weather_information}")

#         return{
#          "statusCode" : 200,
#          "body" : json.dumps({
#             "message" : "Weather information was successfully fetched",
#             "data" : Weather_information
#          })
#         } 
        
#     except Exception as e:
#         print(f"Error : {e}")
#         return{
#           "statusCode" : 500,
#           "body" : json.dumps({
#              "message" : "Weather information was not successfully fetched",
#              "error" : str(e)
#         })
#         }

# for x in range(3):
   
#    for y in range(1,10):
#                 print(y, end="")
#    print(".")
    
    # sns_client = boto3.client('sns')
    # sns_arn = os.getenv("sns_arn")
    
    # if temp >= threshold : 
    #   alert_message = {
    #     "city": Weather_information["city"],
    #     "country": Weather_information["country"],
    #     "temperature": Weather_information["temperature"],
    #     "message": "Temperature threshold exceeded!"
    # }
      
    #   sns_client.publish(
    #      TopicArn = sns_arn,
    #      message=json.dumps(alert_message),
    #      Subject="High temperature alert" 
    #   )
    #      print("Alert sent to subscriber in SNS Topic")
    
    
    This codebase lives in aws lambda and is triggered by an event to fetch weather data from an external API and store it in a MongoDB database. It also includes error handling and logging for better monitoring and debugging.