# Weather Application Project

This project is designed to apply various concepts related to _object-oriented design_, _RESTFul APIs_, and _Model-Template-Controller_ architecture. The application provides users with access to accurate and up-to-date weather data and forecasts, personalized user experiences, and administrative functionalities.

## Table of Contents

- [Business Model](#business-model)
- [User Stories](#user-stories)
- [Entities](#entities)
- [Web Services](#web-services)

## Business Model

This is an application that provides users with access to accurate and up-to-date weather data and future weather forecasts. It also allows users to register personalized accounts, offering a more relevant experience tailored to their individual preferences.

## User Stories

- **As a user, I want to be able to register in the app**, so what further personalize my experience and access additional features.
- **As a user, I want to be able to log in to the application**, so what have a more personalized experience.
- **As an administrator, I want to be able to see the record of all the users of the application and their data**, so what manage user information and have control in the application.
- **As a user, I want to be able to see the current weather of my location**, including temperature, weather conditions (sunny, cloudy, rainy, etc.), and wind chill, so what have the necessary information about the weather in my location.
- **As a user, I want to receive a future weather forecast for my location**, showing the expected temperature, weather conditions, and any significant changes, so what know the weather changes during the day.
- **As a user, I want to be able to check the weather at other specific locations**, either by manually entering the location or selecting it on an interactive map.
- **As a user, I want to have access to additional weather details**, such as humidity, wind speed, etc., so what have all the weather information in a single application.
- **As a user, I want the option to receive notifications about significant weather changes**, such as storm alerts, drastic temperature changes, or adverse weather conditions.
- **As a user, I want to customize the unit of measurement for temperature, wind speed, and other relevant measurements**, so what personalize the user experience.

## Entities

- **Administrator**: 
  - Attributes: name
  - Methods: view users, view user data

- **User**: 
  - Attributes: username, password, location, unit of measurement preference, logged in/not logged in, receive notifications
  - Methods: register, login, update preferences, view weather data

- **Weather Data**: 
  - Attributes: temperature, sensation, weather condition, humidity, wind speed
  - Methods: request current weather data, request forecast data, send weather notifications

## Web Services

- **Get Weather Data**:
  - Endpoint: `/get_weather_data`
  - HTTP Method: `GET`
  - Request: `{ "location": "string" }`
  - Response: `{ "temperature": float, "feels_like": float, "weather_condition": "string", "humidity": float, "wind_speed": float }`

- **Get Forecast Data**:
  - Endpoint: `/get_weather_forecast`
  - HTTP Method: `GET`
  - Request: `{ "time": "string", "location": "string" }`
  - Response: `{ "temperature": float, "feels_like": float, "weather_condition": "string", "humidity": float, "wind_speed": float }`

- **Send Weather Notification**:
  - Endpoint: `/send_weather_notification`
  - HTTP Method: `PUT`
  - Request: `{ "notification": "string" }`

- **Login**:
  - Endpoint: `/login`
  - HTTP Method: `POST`
  - Request: `{ "username": "string", "password": "string" }`

- **Create User**:
  - Endpoint: `/register`
  - HTTP Method: `POST`
  - Request: `{ "username": "string", "password": "string", "location": "string", "preferred_measurement_unit": "string" }`

