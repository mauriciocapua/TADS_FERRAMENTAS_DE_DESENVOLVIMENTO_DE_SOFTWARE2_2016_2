# -*- coding: utf-8 -*-

import sys

from persistencia.conexao import *
from negocio.usuario import *


class UsuarioDAO:
    """
	def __init__(self):
	"""

    def login(self, nome, senha):
        chave = False
        objConexao = Conexao()
        objConexao.cur.execute("SELECT * FROM usuario where nome = (%s) and senha = (%s);",
                               [nome, senha])

        linhasRetornadas = objConexao.cur.rowcount
        if (linhasRetornadas > 0):
            chave = True

        objConexao.fechar()
        return chave
