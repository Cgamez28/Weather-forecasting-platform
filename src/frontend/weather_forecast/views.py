from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def register(request):
    return render(request, 'register.html')

def weather_forecast(request):
    return render(request, 'weather_forecast.html')

def current_weather(request):
    return render(request, 'current_weather.html')