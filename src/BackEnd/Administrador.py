class administrador:
    def __init__(self):
        self.nombre = "Administrador"
        self.__Contraseña = "C0ntr4s3ñ4dm1n"
        self.comprob = False

    def iniciar_sesion(nombre, Contraseña):
        tomar_nombre = str(input("Digite el nombre de usuario"))
        if(tomar_nombre == nombre):
            while comprob == False:
                tomar_contraseña = str(input("Digite su contraseña: "))
                if(tomar_contraseña == Contraseña):
                    comprob = True
                    print("Accedido correctamente")
                else:
                    comprob = False
                    print("Contraseña incorrecta, intentelo nuevamente")


    def cerrar_sesion():
        pass        