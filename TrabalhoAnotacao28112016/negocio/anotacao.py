from config import *
from sqlalchemy import *


# from negocio.imagem import *
# from negocio.relacionamento_usuarioanotacao import *


# import datetime
#
# date = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

class Anotacao():
    def __init__(self, id=None, titulo="", descricao="", data=""):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        # self.imagem = imagem
        self.data = data

    def imprime(self):
        return str(self.id) + " | " + self.titulo + " | " + self.descricao + "| " + str(self.data)
