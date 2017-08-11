class Usuario:
    def __init__(self, id=None, nome="", senha=""):
        self.id = id
        self.nome = nome
        self.senha = senha

    def imprime(self):
        print str(self.id) + " | " + self.nome + " | " + self.senha + " | "
