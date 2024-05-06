import requests
from usuarios_p import Usuario
from pydantic import BaseModel
class Api(BaseModel):
    """
    Esta clase se encarga de comunicarse con la API del clima 
    """
    temperatura: str
    sensacion_termica: str
    humedad: str
    condicion_climatica: str 
    velocidad_viento: str
    _api_key = "081af87fec0c61e0ae4e68e6dc52be4b"
    
    def obtener_datos_clima(self, ubicacion: str):
        """
        Este metodo sera el encargado de obtener los datos del clima mediante la API
        
        Parametros:
            - ubicacion (str): La direccion o nombre de la ciudad a buscar en la API
            
        Retorna:
            Un diccionario el cual contiene los datos de una determinada ubicacion 
        """
        url = f"http://api.openweathermap.org/data/2.5/weather?q={ubicacion}&APPID={self._api_key}"
        res = requests.get(url)
        data = res.json()
        temperatura = self.temperatura = data["main"]["temp"]
        sensacion_termica = self.sensacion_termica = data["main"]["feels_like"]
        humedad = self.humedad = data["main"]["humidity"]
        condicion_climatica = self.condicion_climatica = data["weather"][0]["description"].capitalize()
        velocidad_viento = self.velocidad_viento = data["wind"]["speed"] 
        datosclima = {
            "fecha": "Hoy",
            "temperatura": temperatura,
            "sensación termica": sensacion_termica,
            "humedad": humedad,
            "condición climática": condicion_climatica,
            "velocidad del viento": velocidad_viento
                      }
        return datosclima   
        
        
    def obtener_datos_pronostico(self, ubicacion: str):
        """
        Este metodo sera el encargado de obtener los datos del pronostico del clima
        
        Parametros:
            - ubicacion (str): La direccion o nombre de la ciudad a buscar en la API
            
        Retorna:
            Un diccionario el cual contiene los datos de una determinada ubicacion 
        """
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={ubicacion}&appid={self._api_key}"
        res = requests.get(url) 
        data = res.json()
        temperatura = self.temperatura = data["main"]["temp"]
        sensacion_termica = self.sensacion_termica = data["main"]["feels_like"]
        humedad = self.humedad = data["main"]["humidity"]
        condicion_climatica = self.condicion_climatica = data["list"][0]["weather"][0]["main"].capitalize()
        velocidad_viento = self.velocidad_viento = data["wind"]["speed"] 
        fecha = data["list"][0]["dt_txt"]
        datosclima = {
            "fecha": fecha,
            "temperatura": temperatura,
            "sensación termica": sensacion_termica,
            "humedad": humedad,
            "condición climática": condicion_climatica,
            "velocidad del viento": velocidad_viento
                      }
        return datosclima 
        
    
class DatosClima(Api):
    """
    Esta clase representa los datos del clima 
    """
    
    def __init__(self):
        super().__init__() 
    
    def mostrar_datos_clima(self, datosclima: dict):
        """
        Este metodo sera el encargado de mostrar al usuario los datos del clima
        Parametros:
            - datosclima (dict): El diccionario que contiene todos los datos del clima

        """
        print(f"La temperatura de la fecha ")
    
    def enviar_notificacion_clima(self, Usuario: Usuario, datosclima: dict):
        """
        Este metodo sera el encargado de enviar una notificacion al usuario con los algunos datos del clima actual
        """
        if Usuario.recibir_notificaciones:
            print(f"Hola {Usuario.nombre_usuario}, La temperatura en este momento es de {datosclima["temperatura"]}")