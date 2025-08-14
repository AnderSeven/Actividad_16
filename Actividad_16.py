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
