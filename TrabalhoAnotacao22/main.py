from config import *

from modulo1 import modulo1
from negocio.anotacao import *
from negocio.usuario import *
from flask_admin import BaseView, expose

app.register_blueprint(modulo1, url_prefix='/modulo1')


@app.route("/login")
def login():
    return render_template("formulario_login.html")


@app.route("/")
def inicial():
    # anotacaoDAO = AnotacaoDAO()
    # lista = anotacaoDAO.listar()
    # return render_template("listarAnotacaofree.html", lista=[])
    # return render_template("listarAnotacaofree.html")
    # return redirect(url_for('listarfree'))
    # lista = Anotacao.query.filter(Anotacao.lixeira == False).order_by(Anotacao.data)
    return redirect("admin")


class listarfree(BaseView):
    @expose('/')
    def index(self):
        lista = Anotacao.query.filter(Anotacao.lixeira == False).order_by(Anotacao.data)
        return self.render('admin/default_free.html', lista=lista, tipo='lista')


class lixeirafree(BaseView):
    @expose('/')
    def index(self):
        lista = Anotacao.query.filter(Anotacao.lixeira == True).order_by(Anotacao.data)
        return self.render('admin/default_free.html', lista=lista, tipo='lixeira')


# @app.route("/listarfree")
# def listarfree():
#     # anotacaoDAO = AnotacaoDAO()
#     # lista = anotacaoDAO.listar()
#     lista = Anotacao.query.filter(Anotacao.lixeira == False).order_by(Anotacao.data)
#     return render_template("listarAnotacaofree.html", lista=lista, tipo='lista')
#
#
# @app.route("/lixeirafree")
# def listarLixeira():
#     # anotacaoDAO = AnotacaoDAO()
#
#     lista = Anotacao.query.filter(Anotacao.lixeira == True).order_by(Anotacao.data)
#     return render_template("listarLixeirafree.html", lista=lista, tipo='lixeira')
#
#
# @app.route("/admin")
# def x():
#     return render_template("http://127.0.0.1:5000/admin/")


if __name__ == "__main__":

    # db.drop_all()
    db.create_all()
    # usuario = Usuario(id=None, nome='monstro', senha='37')
    # db.session.add(usuario)
    # usuario = Usuario(id=None, nome='igor', senha='30')
    # db.session.add(usuario)
    # usuario = Usuario(id=None, nome='bambam', senha='birl')
    # db.session.add(usuario)
    db.session.commit()
    admin.add_view(ModelView(Usuario, db.session))
    admin.add_view(ModelView(Anotacao, db.session))
    admin.add_view(ModelView(Imagem, db.session))
    admin.add_view(listarfree(name='Lista de anotacoes'))
    admin.add_view(lixeirafree(name='Lixeira de anotacoes'))

    app.run()


    # criacao de apps flask
    # from flask import Flask
    #
    # # templates
    # from flask import render_template
    #
    # # redirecionamento
    # from flask import redirect, url_for
    #
    # # trabalhando com form
    # from flask import request
    #
    # # trabalhando com session
    # from flask import session
# from flask_sqlalchemy import SQLAlchemy
# import datetime
# import sys
# import datetime
# from persistencia.conexao import *
# from persistencia.usuarioDAO import *
# from negocio.usuario import *
