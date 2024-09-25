class Materia:
    id: str
    nombre: str
    instructor: str
    descripcion: str
    semestre: int
    creditos: int

    def __init__(self, id: str, nombre: str, instructor: str, descripcion: str, semestre: int, creditos: int):
        self.id = id
        self.nombre = nombre
        self.instructor = instructor
        self.descripcion = descripcion
        self.semestre = semestre
        self.creditos = creditos
