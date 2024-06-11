"""This file contains the implementation of the entry point for REST API services."""
from fastapi import FastAPI
from core import WeatherData
from users_p import User
from users_services import router_users
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import requests


app = FastAPI()
app.include_router(router_users)

origins = ["http://localhost", "http://localhost:5500"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/get_weather_data")
def get_weather_data(location: str) -> dict:   
    """
    This method will be responsible for obtaining weather data through the API.
    
    Parameters:
        - location (str): The address or name of the city to search in the API
        
    Returns:
        A dictionary containing data for a specific location.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&APPID=081af87fec0c61e0ae4e68e6dc52be4b"
    res = requests.get(url)
    data = res.json()
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    weather_condition = data["weather"][0]["description"].capitalize()
    wind_speed = data["wind"]["speed"]
    weather_data = {
        "date": "Today",
        "temperature": temperature,
        "feels like": feels_like,
        "humidity": humidity,
        "weather condition": weather_condition,
        "wind speed": wind_speed
    }
    return weather_data 

@app.get("/get_forecast_data")
def get_forecast_data(time:str, location: str) -> dict:   
    """
    This method will be responsible for obtaining the weather forecast data.
    
    Parameters:
        - location (str): The address or name of the city to search in the API
        - time (str): time 
    Returns:
        A dictionary containing data for a specific location.
    """
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid=081af87fec0c61e0ae4e68e6dc52be4b"
    res = requests.get(url)
    data = res.json()
    date = time
    for i in range(len(data['list'])):
        if data['list'][i]['dt_txt'] == time:
            temperature = data['list'][i]['main']['temp']
            feels_like = data['list'][i]['main']['feels_like']
            humidity = data['list'][i]['main']['humidity']
            weather_condition = data['list'][i]['weather'][0]['description']
            wind_speed = data['list'][i]['wind']['speed']
    forecast_data = {
        "date": date,
        "temperature": temperature,
        "feels like": feels_like,
        "humidity": humidity,
        "weather condition": weather_condition,
        "wind speed": wind_speed
    }
    return forecast_data

@app.post("/send_weather_notification")
def send_weather_notification(user: User, weather_data: dict):   
    """
    This method will be responsible for showing the user the weather data.
    
    Parameters:
        - user (User): The user object containing user information.
        - weather_data (dict): The dictionary containing all the weather data.
    """
    if user.receive_notifications == 'True':
            return {"message": f"Hello {user.username}, The current temperature is {weather_data['temperature']}"}

if __name__ == "__main__":   
    uvicorn.run(app, host="0.0.0.0", port=8080)