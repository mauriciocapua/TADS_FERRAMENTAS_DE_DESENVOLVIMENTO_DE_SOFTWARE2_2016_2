from config import *
from sqlalchemy import *

# from negocio.usuario import *
# from negocio.anotacao import *

relacionamento_usuarioanotacao = db.Table('relacionamento_usuarioanotacao',

                                          db.Column('usuario_id', db.Integer, db.ForeignKey('usuario.id'),
                                                    nullable=False),
                                          db.Column('anotacao_id', db.Integer, db.ForeignKey('anotacao.id'),
                                                    nullable=False),
                                          db.PrimaryKeyConstraint('usuario_id', 'anotacao_id')
                                          )
