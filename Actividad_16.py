class biblioteca():
    def __init__(self, titulo, autor, ano, codigo):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.codigo = codigo

    def info_libro(self):
        return f"Titulo: {self.titulo}, "