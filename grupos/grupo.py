from typing import List
from estudiantes.estudiante import Estudiante
from materias.materia import Materia
from maestros.maestro import Maestro

class Grupo:
    id:int

    estudiantes: List[Estudiante] = []
    maestros: List[Maestro] = []
    materias: List[Materia] = []
    tipo: chr

