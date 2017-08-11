from config import *
from sqlalchemy import *
from negocio.imagem import *
from negocio.relacionamento_usuarioanotacao import *


# import datetime
#
# date = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

class Anotacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.Text)
    descricao = db.Column(db.Text)
    data = db.Column(db.DateTime(timezone=False))
    lixeira = db.Column(db.Boolean, default=False)
    # imagem = db.Column(db.Text)
    imagem = db.relationship('Imagem', backref='anotacao', cascade="all, delete-orphan")

    def __init__(self, id=None, titulo="", descricao="", data=""):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        # self.imagem = imagem
        self.data = data

    def imprime(self):
        print str(self.id) + " | " + self.titulo + " | " + self.descricao + + str(self.data)

    def deletarAnotacao(self):
        db.session.delete(self)
        db.session.commit()

    def addImagem(self, filename):
        imagem = Imagem(None, filename, self.id)
        db.session.add(imagem)
        db.session.commit()
