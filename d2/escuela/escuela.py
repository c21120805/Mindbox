from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint
from carrera.carrera import Carrera
from semestre.semestre import Semestre

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_grupos: List[Grupo] = []
    lista_materias: List[Materia] = []
    lista_carreras: List[Carrera] = []
    lista_semestre: List[Semestre] = []

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

    def eliminar_maestro(self, numero_control_maestro: str):
        for maestro in self.lista_maestros:
            if maestro.numero_control == numero_control_maestro:
                self.lista_maestros.remove(maestro)
                print("maestro eliminado")
                return
        print(f"no se encontro maestro con no. control: {numero_control_maestro}")

    def registrar_materia(self):
        self.lista_materias.append(Materia)

    def generar_id(self):
        ultimas_letras_id = Materia.nombre[-2:].upper()
        semestre = Materia.semestre
        credito = Materia.creditos
        aleatorio = randint(1, 1000)
        id_materia = f"MT{ultimas_letras_id}{semestre}{credito}{aleatorio}"
        return id_materia

    def listar_materias(self):
        print("************* Materias *************")    
        for materias in self.lista_materias:
            print(materias.mostrar_info_materia())

    def eliminar_materia(self, id_materia: str):
        for materia in self.lista_materias:
            if materia.id == id_materia.strip():
                self.lista_materias.remove(materia)
                print(f"Materia {materia.nombre}, eliminado exitosamente.\n")
                return 

    def registrar_carrera(self, carrera: Carrera):
        self.lista_carreras.append(carrera)
    
    def listar_carreras(self):
        print("*************Carreras*************")
        for carrera in self.lista_carreras:
            print(carrera.mostrar_info_carrera())
        #SEMESTRE
    def registrar_semestre(self, semestre: Semestre):
        id_carrera = semestre.id_carrera
        for carrera in self.lista_carreras:
            if carrera.matricula == id_carrera:
                carrera.registrar_semestre(semestre=semestre)
                break
        self.lista_semestre.append(semestre)

    def listar_semestres(self):
        print("*************Semestres*************")
        for semestre in self.lista_semestre:
            print(semestre.mostrar_info_semestre())
            
          #GRUPOS
    def registrar_grupo(self, grupo: Grupo):
        id_semestre = grupo.id_semestre

        for semestre in self.lista_semestre:
            if id_semestre == semestre.id:
                semestre.registrar_grupo_en_semestre(grupo=grupo)
                break
        self.lista_grupos.append(grupo)
    
    def listar_grupos(self):
        print("** Grupos **")   
        for grupo in self.lista_grupos:  
            print(grupo.mostrar_info_grupo())
        


    

