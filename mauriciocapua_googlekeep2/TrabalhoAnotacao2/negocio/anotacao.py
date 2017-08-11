class Anotacao:
    def __init__(self, id=None, titulo="", descricao="", data=""):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
    def imprime(self):
        print str(self.id) + " | " + self.titulo + " | " + self.descricao + " | " + str(self.data)

