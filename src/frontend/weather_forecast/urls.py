from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('weather_forecast/', views.weather_forecast, name='weather_forecast'),
    path('current_weather/', views.current_weather, name='current_weather'),
    path('admin/', views.admin, name='admin')
]