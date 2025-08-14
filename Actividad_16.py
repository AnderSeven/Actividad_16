class biblioteca():
    def __init__(self, titulo, autor, ano, codigo):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.codigo = codigo

    def info_libro(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Año de publicacion: {self.ano}, Codigo: {self.codigo}"

class usuarios():
    def __init__(self, nombre, carnet, carrera):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera

    def info_usuarios(self):
        return f"Nombre: {self.nombre}, Carnet: {self.carnet}, Carrera: {self.carrera}"

class registro_estudiantes:
    def __init__(self):
        self.lista_biblioteca = []

    def registrar(self):
        nombre = input("Ingrese el nombre: ")
        carnet = int(input("Ingrese el carnet: "))
        carrera = input("Ingrese la carrera: ")

    def info(self):
        if len(self.lista_biblioteca) > 0:
            print("---Lista de Estudiantes---")
            for i in self.lista_biblioteca:
                print(f"")
        else:
            print("No hay estudiantes registrados")

class prestamos():
    pass

class devoluciones():
    pass


a = False
opciones = 0
while a == False:
    print("---Menu---")
    print("1. Agregar estudiante")
    print("2. Agregar libro")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Salir")
    opciones = int(input("Elija una opcion: "))
    match opciones:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            print("Gracias por usar el sistema")
            a = True
        case _:
            print("Opcion invalida")