"""This file contains the implementation of the entry point for REST API services."""
from fastapi import FastAPI
from core import WeatherData
from users_p import User
from BackEnd.users_services import router_catalog

app = FastAPI()
app.include_router(router_catalog)

@app.post("/get_weather_data")
def get_weather_data(location: str) -> dict:   
    """
    This method will be responsible for obtaining weather data through the API.
    
    Parameters:
        - location (str): The address or name of the city to search in the API
        
    Returns:
        A dictionary containing data for a specific location.
    """
    return WeatherData().get_weather_data(location)

@app.post("/get_forecast_data")
def get_forecast_data(location: str) -> dict:   
    """
    This method will be responsible for obtaining the weather forecast data.
    
    Parameters:
        - location (str): The address or name of the city to search in the API
        
    Returns:
        A dictionary containing data for a specific location.
    """
    return WeatherData().get_forecast_data(location)

@app.post("/send_weather_notification")
def send_weather_notification(user: User, weather_data: dict):   
    """
    This method will be responsible for showing the user the weather data.
    
    Parameters:
        - user (User): The user object containing user information.
        - weather_data (dict): The dictionary containing all the weather data.
    """
    return WeatherData().send_weather_notification(user, weather_data)
