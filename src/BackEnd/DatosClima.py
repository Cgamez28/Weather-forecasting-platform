import requests


class Api:
    def __init__(self):
        self.temperatura =  None
        self.sensacion_termica = None
        self.condicion_climatica = None
        self.humedad = None
        self.velocidad_viento = None
        self.api_key = "081af87fec0c61e0ae4e68e6dc52be4b"
    
    def obtener_datos_clima(self, ubicacion: str):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={ubicacion},uk&APPID={self.api_key}"
        res = requests.get(url)
        data = res.json()
        self.temperatura = data["main"]["temp"]
        self.sensacion_termica = data["main"]["feels_like"]
        self.humedad = data["main"]["humidity"]
        self.condicion_climatica = data["weather"][0]["description"].capitalize()
        self.velocidad_viento = data["wind"]["speed"]
        
        
        
        
    def obtener_datos_pronostico(self, ubicacion):
        pass
    
class DatosClima(Api):
    def __init__(self):
        super().__init__(
        temperatura =  None,
        sensacion_termica = None,
        condicion_climatica = None,
        humedad = None,
        velocidad_viento = None
        ) 
    
    def mostrar_datos_clima(self, temperatura, sensacion_termica, condicion_climatica, humedad, velocidad_viento):
        pass
    
    def enviar_notificacion_clima(self):
        pass