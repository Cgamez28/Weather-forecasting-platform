""" This file contains the attributes and methods of the WeatherData class """
import requests
from users_p import User 
from pydantic import BaseModel

class WeatherData(BaseModel):
    """
    This class is responsible for communicating with the API and obtaining the necessary weather data
    """
    temperature: str
    feels_like: str
    humidity: str
    weather_condition: str 
    wind_speed: str
    _api_key = "081af87fec0c61e0ae4e68e6dc52be4b"
    
    def get_weather_data(self, location: str):
        """
        This method will be responsible for obtaining weather data through the API
        
        Parameters:
            - location (str): The address or name of the city to search for in the API
            
        Returns:
            A dictionary containing data for a specific location
        """
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&APPID={self._api_key}"
        res = requests.get(url)
        data = res.json()
        temperature = self.temperature = data["main"]["temp"]
        feels_like = self.feels_like = data["main"]["feels_like"]
        humidity = self.humidity = data["main"]["humidity"]
        weather_condition = self.weather_condition = data["weather"][0]["description"].capitalize()
        wind_speed = self.wind_speed = data["wind"]["speed"]
        weather_data = {
            "date": "Today",
            "temperature": temperature,
            "feels like": feels_like,
            "humidity": humidity,
            "weather condition": weather_condition,
            "wind speed": wind_speed
        }
        return weather_data   
        
    def get_forecast_data(self, time: str, location: str):
        """
        This method will be responsible for obtaining the weather forecast data

        Parameters:
            - location (str): The address or name of the city to search for in the API
            
        Returns:
            A dictionary containing data for a specific location
        """
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={self._api_key}"
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
    
    def send_weather_notification(self, user: User, weather_data: dict):
        """
        This method will be responsible for sending a notification to the user with some current weather data
        """
        if user.receive_notifications:
            print(f"Hello {user.username}, The current temperature is {weather_data['temperature']}")
