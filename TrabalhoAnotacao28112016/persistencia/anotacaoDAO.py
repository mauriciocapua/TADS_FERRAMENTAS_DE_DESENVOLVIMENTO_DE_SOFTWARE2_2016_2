# -*- coding: utf-8 -*-

# import sys
#
# sys.path.append("../negocio")
# sys.path.append("../persistencia")
#
# from conexao import *
# from negocio.anotacao import *

from negocio.anotacao import *
from persistencia.conexao import *


class AnotacaoDAO:
    def listar(self):
        objConexao = Conexao()
        objConexao.cur.execute("SELECT * FROM anotacao where lixeira = 'FALSE' order by data;")
        lista = []
        linhasRetornadas = objConexao.cur.rowcount
        i = 0
        while (i < linhasRetornadas):
            registro = objConexao.cur.fetchone()
            # (self, id = None, titulo = "", descricao = "", data = "", imagem = ""):
            lista.append(Anotacao(registro[0], registro[1], registro[2], registro[3]))
            i += 1
        objConexao.fechar()
        return lista

    def listarUm(self):
        objConexao = Conexao()
        objConexao.cur.execute("SELECT * FROM anotacao where id = 1;")
        anotacao = null
        linhasRetornadas = objConexao.cur.rowcount
        i = 0
        while (i < 1):
            registro = objConexao.cur.fetchone()
            # (self, id = None, titulo = "", descricao = "", data = "", imagem = ""):
            anotacao = Anotacao(registro[0], registro[1], registro[2], registro[3])
            i += 1
        objConexao.fechar()
        return anotacao

    def listar_data(self):
        objConexao = Conexao()
        objConexao.cur.execute("SELECT * FROM anotacao where lixeira = false order by data;")
        lista = []
        linhasRetornadas = objConexao.cur.rowcount
        i = 0
        while (i < linhasRetornadas):
            registro = objConexao.cur.fetchone()
            lista.append(Anotacao(registro[0], registro[1], registro[2], registro[3]))
            i += 1
        objConexao.fechar()
        return lista

    def inserir(self, anotacao):
        # abri cursor

        objConexao = Conexao()

        # sql
        objConexao.cur.execute("INSERT INTO anotacao(titulo, descricao, data,imagem) VALUES (%s,%s,%s,%s)",
                               [anotacao.titulo, anotacao.descricao, anotacao.data, anotacao.imagem])

        # comitando
        objConexao.con.commit()

        print "registrado"

        objConexao.fechar()

    def excluir(self, id):
        # criar a conexao
        objConexao = Conexao()

        # sql
        objConexao.cur.execute("UPDATE anotacao SET lixeira = 'TRUE' WHERE id = (%s);", [id])

        # comitando
        objConexao.con.commit()

        print "deletado"

        objConexao.fechar()

    def update(self, id, titulo, descricao, data):
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
        objConexao.cur.execute("UPDATE anotacao SET titulo = (%s), descricao = (%s), data = (%s) WHERE id = (%s);",
                               [titulo, descricao, data, id])
        objConexao.con.commit()
        objConexao.fechar()

    def copiar(self, id):
        objConexao = Conexao()

        objConexao.cur.execute("SELECT * FROM anotacao WHERE id = (%s);", [id])

        registro = objConexao.cur.fetchone()

        anotacao = Anotacao(registro[0], registro[1], registro[2], registro[3])

        objConexao.fechar()

        self.inserir(anotacao)

    """
    LIXEIRA
    """

    def listar_lixeira(self):
        objConexao = Conexao()
        objConexao.cur.execute("SELECT * FROM anotacao where lixeira = 'TRUE' order by data;")
        lista = []
        linhasRetornadas = objConexao.cur.rowcount
        i = 0
        while (i < linhasRetornadas):
            registro = objConexao.cur.fetchone()
            lista.append(Anotacao(registro[0], registro[1], registro[2], registro[3]))
            i += 1
        objConexao.fechar()
        return lista

    def excluir_permanentemente(self, id):
        # criar a conexao
        objConexao = Conexao()

        # sql
        objConexao.cur.execute("DELETE FROM anotacao WHERE id = %s", [id])

        # comitando
        objConexao.con.commit()

        objConexao.fechar()

    def restaurar(self, id):
        # criar a conexao
        objConexao = Conexao()

        # sql
        objConexao.cur.execute("UPDATE anotacao SET lixeira = 'FALSE' WHERE id = (%s);", [id])

        # comitando
        objConexao.con.commit()

        objConexao.fechar()


'''
    def listar_um(self, id):
        objConexao = Conexao()
        objConexao.cur.execute("SELECT * FROM anotacao where id = %s", [id])

        if objConexao.cur.rowcount > 0:

            registro = objConexao.cur.fetchone()
            anotacao = Anotacao(registro[0], registro[1], registro[2], registro[3])

        objConexao.fechar()
        return anotacao
        else:
            objConexao.
'''
