from typing import List
from materias.materia import Materias
from estudiantes.estudiante import Estudiante
from semestre.semestre import Semestre
from random import randint

class Carrera:
    matricula: str
    nombre: str
    materias: List[Materias]
    numero_semestre: int = 0
    semestres: List[Semestre] = []

    def __init__(self, nombre: str):
        self.matricula = self.generar_id(nombre)
        self.nombre = nombre

    def generar_id(self, nombre: chr) -> str:
        return f"{nombre}-{randint(1,100000)}-{randint(0,1000000)}"
    
    def registrar_semestre(self, semestre: Semestre):
        self.numero_semestre += 1
        self.semestres.append(semestre)

    def mostrar_info_carrera(self):
        info_carrera = f"nombre: {self.nombre}, matricula: {self.matricula}, numero_semestre: {self.numero_semestre}"
        return info_carrera