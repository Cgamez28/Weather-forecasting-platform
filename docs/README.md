# Course Project

This is a project to apply different concepts regarding _object-oriented design_, _RESTFul APIs_, and _Model-Template-Controller_.

## Business Model

This is an application that provides users with access to accurate and up-to-date weather data and future weather forecast display, it also allows users to register personalized accounts, giving them a more relevant experience tailored to their individual preferences.

## User Stories

- As a user, I want to be able to register in the app, to further personalize my experience and access additional features.
- As a user, I want the app to be able to access my device's location to receive accurate weather information for that area.
- As a user, I want to be able to see the current weather of my location, including temperature, weather conditions (sunny, cloudy, rainy, etc.), and wind chill, to have the necessary information about the weather in my location
- As a user, I want to receive a future weather forecast for my location, showing the expected temperature, weather conditions and any significant changes, to know the weather changes during the day.
- As a user, I want to be able to check the weather at other specific locations, either by manually entering the location or selecting it on an interactive map.
- As a user, I want to have access to additional weather details, such as humidity, wind speed, UV index, etc., to have all the weather information in a single application
- As a user, I want the option to receive notifications about significant weather changes, such as storm alerts, drastic temperature changes, or adverse weather conditions.
- As a user, I want to customize the unit of measurement for temperature, wind speed and other relevant measurements, to personalize the user experience
- As a user, I want the app to maintain a history of previously viewed locations, to facilitate quick access to previous weather information.

## Entities

- Administrator: name
- User: username, password, location, unit of measurement preference, logged in/not logged in
- Weather data: temperature, sensation, weather condition, humidity, wind speed
- API: request data from the weather api
