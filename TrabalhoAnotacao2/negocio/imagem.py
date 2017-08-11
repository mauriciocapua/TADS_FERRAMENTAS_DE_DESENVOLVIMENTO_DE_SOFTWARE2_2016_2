from config import *


class Imagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    endereco = db.Column(db.Text)
    anotacao_id = db.Column(db.Integer, db.ForeignKey('anotacao.id'))

    def __init__(self, id=None, endereco="", anotacao_id=""):
        self.id = id
        self.endereco = endereco
        self.anotacao_id = anotacao_id

    def deleteImagem(self):
        db.session.delete(self)
        db.session.commit()
