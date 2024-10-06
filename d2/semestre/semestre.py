from typing import List
from materias.materia import Materia
from grupos.grupo import Grupo
from random import randint

class Semestre:
    id: str
    id_carrera: str
    numero: int
    materias: List[Materia]
    grupos: List[Grupo]

    def __init__(self, numero: int):
        self.id

    def generar_id(self, numero_semestre: int) -> str:
        return f"{numero_semestre}-{randint(0, 100000)}-{randint(0, 100000)}"

     def registrar_grupo_en_semestre(self, grupo: Grupo):
        self.grupos.append(grupo)

    def mostrar_info_semestre(self):
         info_semestre = f"Id: {self.id}, numero: {self.numero}, ID_Carrera: {self.id_carrera}"
         return info_semestre