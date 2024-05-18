import requests
from usuarios_p import Usuario
from pydantic import BaseModel
class DatosClima(BaseModel):
    """
    Esta clase se encarga de comunicarse con la API y obtener los datos necesarios del clima 
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
        
        
    def obtener_datos_pronostico(self, tiempo: str, ubicacion: str):
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
        fecha = tiempo
        for i in range(len(data['list'])):
            if data['list'][i]['dt_txt'] == tiempo:
                temperatura = data['list'][i]['main']['temp']
                sensacion_termica = data['list'][i]['main']['feels_like']
                humedad = data['list'][i]['main']['humidity']
                condicion_climatica = data['list'][i]['weather'][0]['description']
                velocidad_viento = data['list'][i]['wind']['speed']
        datosclima = {
            "fecha": fecha,
            "temperatura": temperatura,
            "sensación termica": sensacion_termica,
            "humedad": humedad,
            "condición climática": condicion_climatica,
            "velocidad del viento": velocidad_viento
                        }
        return datosclima  
    
    def enviar_notificacion_clima(self, Usuario: Usuario, datosclima: dict):
        """
        Este metodo sera el encargado de enviar una notificacion al usuario con los algunos datos del clima actual
        """
        if Usuario.recibir_notificaciones:
            print(f"Hola {Usuario.nombre_usuario}, La temperatura en este momento es de {datosclima["temperatura"]}")
        
    