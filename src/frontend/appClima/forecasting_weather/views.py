from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def clima_actual(request):
    return render(request, 'clima_actual.html')

def pronostico_clima(request):
    return render(request, 'pronostico_clima.html')
