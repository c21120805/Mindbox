from usuario.usuario import Usuario
from datetime import datetime
from usuario.utils.roles import Rol

class Maestro(Usuario):
    rfc: str
    sueldo: float
    fecha_nacimiento_maestro: datetime


    def __init__(self, numero_controlp: str, nombre: str, apellido: str, sueldo: float, rfc: str, fecha_nacimiento_maestro: datetime, contrasenia: str):
        super().__init__(numero_controlp=numero_controlp, nombre=nombre, apellido=apellido, contrasenia=contrasenia, rol=Rol.MAESTRO)
        self.rfc = rfc
        self.sueldo = sueldo
        self.fecha_nacimiento_maestro = fecha_nacimiento_maestro
      

    def mostrar_info_maestros(self):
        nombre_completo = f"{self.nombre}{self.apellido}"
        info = f"Numero de control: {self.numero_controlp}, nombre completo: {nombre_completo}, sueldo: {self.sueldo},rfc: {self.rfc}, fecha de nacimiento: {self.fecha_nacimiento}"
        return info
