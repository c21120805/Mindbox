from datetime import datetime
from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Estudiante:
    numero_control: str
    nombre: str
    apellido: str
    curp: str
    fecha_nacimiento: datetime
    contrasenia: str
    rol = Rol.ESTUDIANTE

    def __init__(self, numero_control: str, nombre: str, apellido: str, curp: str, fecha_nacimiento: datetime, contrasenia: str, rol = Rol.ESTUDIANTE ):
        self.numero_control = numero_control
        self.nombre = nombre
        self.apellido = apellido
        self.curp = curp 
        self.fecha_nacimiento = fecha_nacimiento
        self.contrasenia = contrasenia

    def mostrar_info_estudiante(self):
        nombre_completo = f"{self.nombre}{self.apellido}"
        info = f"Numero de control: {self.numero_control}, nombre completo: {nombre_completo}, curp: {self.curp}, fecha de nacimiento: {self.fecha_nacimiento}"
        return info