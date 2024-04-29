class Usuarios:
     def __init__(self):
        self.nombre_usuario = None
        self.contraseña = None
        self.ubicacion = None
        self.recibir_notificaciones = True
        self.preferencia_unidad_de_medida = None

    def crear_usuario(nombre_usuario, contraseña, ubicacion, tomar_recibir_notificaciones, comprob = bool):
        """Este metodo será el encargado de realizar la creacion del usuario"""
        nombre_usuario = str(input("Digite el nombre de usuario: "))
        contraseña = str(input("Digite su contraseña: "))
        ubicacion = str(input("Seleccione su ubicacion: "))
        while comprob == False :
            tomar_recibir_notificaciones = str(input("¿Desea recibir notificaciones? (1:si, 2:no)"))
            if(tomar_recibir_notificaciones == 1):
             recibir_notificaciones = True
             comprob = True
            if(tomar_recibir_notificaciones == 2 ):
             recibir_notificaciones = False
             comprob = True
            else:
                print("Error al seleccionar elija nuevamente, recuerde (1:si, 2:no)")
                comprob = False
                
    @staticmethod
    def iniciar_sesion(nombre_usuario, contraseña):
        """
        Este metodo sera usado para el login en la aplicación

        Args:
            nombre_usuario (str): El nombre de usuario
            contraseña (str): La contraseña respectiva al nombre de usuario
        """
        pass

    def cerrar_sesion(self):
        pass