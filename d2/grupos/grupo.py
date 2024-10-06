from typing import List
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materias
from random import randint

class Grupo:
    id: int
    estudiantes: List[Estudiante] = []
    maestros: List[Maestro] = []
    materias: List[Materias] = []
    tipo: chr
    id_semestre: str


    def __init__(self, tipo: chr, id_semestre: str):
        self.id= self.generar_id(tipo=tipo)
        self.tipo = tipo
        self.id_semestre = id_semestre

    def generar_id(self, tipo: chr) -> str:
        return f"{tipo}-{randint(1,100000)}-{randint(0,1000000)}"
    
    def mostrar_info_grupo(self):
        mostrar_info_grupo = f"ID: {self.id},Tipo: {self.tipo},ID semestre: {self.id_semestre}"
        return mostrar_info_grupo
