from Faker import Faker
import random

faker = Faker()

#crea los datos necesarios de un usuario
def generar_usuario():
    usuario = {}
    usuario['nombre'] = faker.user_name()
    usuario['contraseña'] = faker.password(length=10)  
    usuario['ubicacion'] = faker.city()
    usuario['recibir_notificaciones'] = random.choice(['Sí', 'No'])
    usuario['preferencia_unidad'] = random.choice(['Celsius', 'Fahrenheit', 'Kelvin'])
    return usuario

# genera los datos para 10 usuarios
usuarios = [generar_usuario() for _ in range(10)]

# imprime los datos de los usuarios
for i, usuario in enumerate(usuarios, start=1):
    print(f"Usuario {i}:")
    print("Nombre:", usuario['nombre'])
    print("Contraseña:", usuario['contraseña'])
    print("Ubicación:", usuario['ubicacion'])
    print("Recibir notificaciones:", usuario['recibir_notificaciones'])
    print("Preferencia de unidad de medida:", usuario['preferencia_unidad'])
    print()