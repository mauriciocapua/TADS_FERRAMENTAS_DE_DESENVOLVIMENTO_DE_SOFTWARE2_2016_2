# -*- coding: utf-8 -*-

import sys

from persistencia.conexao import *
from negocio.usuario import *


class UsuarioDAO:
    def listar(self):
        objConexao = Conexao()
        objConexao.cur.execute("SELECT * FROM usuario order by id;")
        lista = []
        linhasRetornadas = objConexao.cur.rowcount
        i = 0
        while (i < linhasRetornadas):
            registro = objConexao.cur.fetchone()
            # (self, id = None, titulo = "", descricao = "", data = "", imagem = ""):
            lista.append(Usuario(registro[0], registro[1]))
            i += 1
        objConexao.fechar()
        return lista

    def inserir(self, usuario):
        # abri cursor

        objConexao = Conexao()

        # sql
        objConexao.cur.execute("INSERT INTO usuario(nome) VALUES (%s)",
                               [usuario.nome])

        # comitando
        objConexao.con.commit()

        print "registrado"

        objConexao.fechar()

    def excluir(self, usuario):
        # criar a conexao
        objConexao = Conexao()

        # sql
        objConexao.cur.execute("DELETE FROM usuario WHERE id = (%s);", [usuario.id])

        # comitando
        objConexao.con.commit()

        print "deletado"

        objConexao.fechar()

    def update(self, usuario):
        objConexao = Conexao()
        # objConexao.cur.execute("SELECT * FROM anotacao WHERE id = (%s);", [id])
        # registro = objConexao.cur.fetchone()
        # anotacao = Anotacao(registro[0], registro[1], registro[2], registro[3])
        #  titulo = raw_input('Digite o novo tÃ­tulo: ')
        # data = raw_input('Digite a nova data: ')
        # descricao = raw_input('Digite a nova descriÃ§Ã£o: ')
        # if titulo:
        #     anotacao.titulo = titulo
        # if data:
        #     anotacao.data = data
        # if descricao:
        #     anotacao.descricao = descricao
        objConexao.cur.execute("UPDATE usuario SET nome = (%s) WHERE id = (%s);",
                               [usuario.nome, usuario.id])
        objConexao.con.commit()
        objConexao.fechar()
