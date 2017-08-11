from config import *
from sqlalchemy import *

from negocio.relacionamento_usuarioanotacao import *


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    senha = db.Column(db.Text)
    anotacao = db.relationship('Anotacao', secondary=relacionamento_usuarioanotacao, backref='Usuario')

    def __init__(self, id=None, nome="", senha=""):
        self.id = id
        self.nome = nome
        self.senha = senha

    def imprime(self):
        print str(self.id) + " | " + self.nome + " | " + self.senha + " | "

    def addAnotacao(self, Anotacao):
        self.anotacao.append(Anotacao)
        self.query.filter(Usuario.id == self.id).update
        db.session.commit()

    def deleteAnotacao(self, Anotacao):
        self.anotacao.remove(Anotacao)
        self.query.filter(Usuario.id == self.id).update
        db.session.commit()
