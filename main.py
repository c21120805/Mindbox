from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime

escuela = Escuela()

while True:
    print("\n Mindbox")
    print("1. Registrar estudiante")
    print("2. Registrar maestro")
    print("3. Registrar materia")
    print("4. Registrar grupo")
    print("5. Registrar horario")
    print("6. Mostrar estudiantes")
    print("7.Mostrar maestros")
    print("8.Mostrar materias")
    print("9.Mostrar grupos")
    print("10.Eliminar estudiante")
    print("11.Eliminar maestro")
    print("12.Eliminar materias")
    print("13. Salir")

    opcion = input("Ingresa una opcion para continuar: ")

    if opcion == "1":
        print("Seleccionaste la opcion para registrar un estudiante")

        numero_control = escuela.generar_numero_control()

        print(numero_control)

        nombre = input("Ingresa el nombre: " )
        apellido = input("Ingresa el apellido del estudiante: ")
        curp = input("Ingresar la curp del estudiante: ")
        ano = int(input("Ingresa el ano de nacimiento del estudiante: "))
        mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
        dia = int(input("Ingresa el dia de nacimiento del estudiante: "))
        fecha_nacimiento = datetime(ano, mes, dia)

    elif opcion == "2":
        print("Seleccionaste la opcion para registrar un maestro")

        numero_control = escuela.generar_numero_control()

        print(numero_control)

        nombre = input("Ingresa el nombre: " )
        apellido = input("Ingresa el apellido del maestro: ")
        curp = input("Ingresar la curp del maestro: ")
        ano = int(input("Ingresa el ano de nacimiento del maestro: "))
        mes = int(input("Ingresa el mes de nacimiento del maestro: "))
        dia = int(input("Ingresa el dia de nacimiento del maestro: "))
        fecha_nacimiento = datetime(ano, mes, dia)

    elif opcion == "3":
          
        nombre = input("Ingresar nombre de la materia")
        semestre = int(input("Ingresa no. semestre que la cursa"))
        instructor = input("Ingresa instructor de la materia")
        creditos = int(input("Ingresa no. creditos de la materia"))
        descripcion = input("Ingresa descripcion de la materia")
        materia = Materia(nombre=nombre, instructor=instructor, descripcion=descripcion, semestre=semestre, creditos=creditos)
        id_materia = escuela.generar_id(materia)
        print(f"EL ID de la materia es: ", id_materia)
        materia.id = id

    elif opcion == "4":
        pass
    elif opcion == "5":
        pass
    elif opcion == "6":
        print("Hasta luego")
        break








