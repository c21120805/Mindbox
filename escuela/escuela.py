from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_grupos: List[Grupo] = []
    lista_materias: List[Materia] = []

    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)

    def lista_estudiantes(self):
        print("Estudiantes")
        for estudiante in self.lista_estudiantes:
            print(estudiante.mostrar_info_estudiante())

    def eliminar_estudiante(self, numero_control: str):

        for estudiante in self.lista_estudiantes:
            if estudiante.numero_control == numero_control:
                self.lista_estudiantes.remove(estudiante)
                print("Estudiante eliminado")
                return

        print("No se encontro estudiante con numero de control: {numero_control}")

    def generar_numero_control(self):
        ano = datetime.now().year
        mes = datetime.now().month
        longitud_mas_uno = len(self.lista_estudiantes) + 1
        aleatorio = randint(0, 10000)
        numero_control = ano, mes, longitud_mas_uno, aleatorio
        return numero_control

    def registrar_maestro(self, maestro: Maestro):
        self.lista_maestros.append(maestro)

    def generar_numero_control_maestro(self, rfc: str):
        ano = datetime.now().year
        dia_actual = datetime.now().day
        longitud_mas_uno = len(self.lista_maestros) + 1
        ultimas_letras_rfc = rfc[-2:]
        aleatorio = randint(500, 5000)
        numero_control_maestro = ano, dia_actual, longitud_mas_uno, ultimas_letras_rfc, aleatorio
        return numero_control_maestro

    def registrar_materia(self):
        self.lista_materias.append(Materia)1

    def generar_id(self):
        ultimas_letras_id = materia.nombre[-2:].upper()
        semestre = materia.semestre
        credito = materia.creditos
        aleatorio = randint(1, 1000)
        id_materia = f"MT{ultimas_letras_id}{semestre}{credito}{aleatorio}"
        return id_materia


    

