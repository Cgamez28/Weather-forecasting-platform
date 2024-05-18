from fastapi import FastAPI
from usuarios_p import Usuario, Administrador
from core import DatosClima
from pydantic import BaseModel
from usuarios_services import router_catalog

app = FastAPI()
app.include_router(router_catalog)

@app.post("/obtener_datos_clima")
def obtener_datos_clima(ubicacion: str) -> dict :   
    """
    Este metodo sera el encargado de obtener los datos del clima mediante la API
    
    Parametros:
        - ubicacion (str): La direccion o nombre de la ciudad a buscar en la API
        
    Retorna:
        Un diccionario el cual contiene los datos de una determinada ubicacion 
    """
    return DatosClima.obtener_datos_clima(ubicacion)

@app.post("/obtener_datos_pronostico")
def obtener_datos_pronostico(ubicacion: str) -> dict :   
    """
    Este metodo sera el encargado de obtener los datos del pronostico del clima
    
    Parametros:
        - ubicacion (str): La direccion o nombre de la ciudad a buscar en la API
        
    Retorna:
        Un diccionario el cual contiene los datos de una determinada ubicacion 
    """
    return DatosClima.obtener_datos_pronostico(ubicacion)

@app.post("/enviar_notificacion_clima")
def enviar_notificacion_clima(Usuario: Usuario, datosclima: dict):   
    """
    Este metodo sera el encargado de mostrar al usuario los datos del clima
    Parametros:
        - datosclima (dict): El diccionario que contiene todos los datos del clima

    """
    return DatosClima.enviar_notificacion_clima(Usuario, datosclima)