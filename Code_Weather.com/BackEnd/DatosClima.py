class Api:
    def __init__(self, temperatura: float, sensacion_termica: float, condicion_climatica, humedad: float, velocidad_viento: float):
        self.temperatura =  temperatura
        self.sensacion_termica = sensacion_termica
        self.condicion_climatica = condicion_climatica
        self.humedad = humedad
        self.velocidad_viento = velocidad_viento
    
    def obtener_datos_clima(self, ubicacion):
        pass
    
    def obtener_datos_pronostico(self, ubicacion):
        pass
    
class DatosClima(Api):
    def __init__(self):
        super().__init__() 
    
    def mostrar_datos_clima(self, temperatura, sensacion_termica, condicion_climatica, humedad, velocidad_viento):
        pass
    
    def enviar_notificacion_clima(self):
        pass