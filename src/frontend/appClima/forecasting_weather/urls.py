from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('clima_actual/', views.clima_actual, name='clima_actual'),
    path('pronostico_clima/', views.pronostico_clima, name='pronostico_clima'),
]