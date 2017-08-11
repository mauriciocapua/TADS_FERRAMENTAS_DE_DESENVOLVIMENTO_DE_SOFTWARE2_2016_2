import sys
import datetime
from flask import *

app = Flask(__name__)

import datetime

from negocio.anotacao import *
from persistencia.anotacaoDAO import *
from persistencia.conexao import *
from persistencia.usuarioDAO import *
from negocio.usuario import *

# @app.route("/")
# def index():
#     return render_template("index.html")

data = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')


@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']


@app.route("/listar")
def listar(name=None, mensagem=None):
    if g.user:
        anotacaoDAO = AnotacaoDAO()
        lista = anotacaoDAO.listar()
        return render_template("listarAnotacao.html", name=session.get('user'), lista=lista, mensagem=mensagem)
    else:
        return render_template("formulario.html")


@app.route("/listarLixeira")
def listarLixeira(name=None, mensagem=None):
    if g.user:
        anotacaoDAO = AnotacaoDAO()
        lista = anotacaoDAO.listar_lixeira()
        return render_template("listarLixeira.html", name=session.get('user'), lista=lista, mensagem=mensagem)
    else:
        return render_template("formulario.html")


@app.route("/formularioAnotacao")
def formularioAnotacao():
    if g.user:
        return render_template("adicionarAnotacao.html")
    else:
        return render_template("formulario.html")


@app.route("/adicionarAnotacao", methods=['POST'])
def adicionar(tituloAnotacao=None, descricaoAnotacao=None):
    if g.user:
        error = None
        if request.form['tituloAnotacao'] != None:
            if request.form['descricaoAnotacao'] != None:
                anotacao = Anotacao(None, request.form['tituloAnotacao'], request.form['descricaoAnotacao'], data)
                anotacaoDAO = AnotacaoDAO()
                anotacaoDAO.inserir(anotacao)
                mensagem = "anotacao inserida"
                return redirect(url_for('listar', name=None, mensagem=mensagem))
            else:
                error = "descricao vazia"
                return redirect(url_for('formularioAnotacao', error=error))
        else:
            error = "titulo vazio"
            return redirect(url_for('formularioAnotacao', error=error))
    else:
        return render_template("formulario.html")


@app.route("/acao", methods=['POST'])
def manipula():
    if g.user:
        anotacaoDAO = AnotacaoDAO()
        url = 'listar'
        mensagem = None
        if request.form['funcao'] == 'deletar':
            anotacaoDAO.excluir(request.form['button'])
            mensagem = "deletado"
        elif request.form['funcao'] == 'alterar':
            if request.form['alteracao'] == 'ok':
                anotacaoDAO.update(request.form['id'], request.form['titulo'], request.form['descricao'],
                                   request.form['data'])
                mensagem = "alterado"
                url = 'listarLixeira'
            else:
                return render_template('alterarAnotacao.html')
        elif request.form['funcao'] == 'deletar permanentemente':
            anotacaoDAO.excluir_permanentemente(request.form['button'])
            mensagem = "deletado permanentemente"
            url = 'listarLixeira'
        elif request.form['funcao'] == 'restaurar':
            anotacaoDAO.restaurar(request.form['button'])
            mensagem = "restaurado"
            url = 'listarLixeira'
        else:
            mensagem = "nao deu"
        return redirect(url_for(url, name=None, mensagem=mensagem))
    else:
        return render_template("formulario.html")


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user', None)
    return render_template('formulario.html', error='You were logged out')


@app.route("/")
def index():
    return render_template("formulario.html")


@app.route("/session", methods=['POST'])
def login(nome=None, senha=None):
    error = None
    usuarioDAO = UsuarioDAO()

    if usuarioDAO.login(request.form['username'], request.form['password']) == False:
        error = 'Invalid LOGIN'
    else:
        session['logged_in'] = True
        session['user'] = request.form['username']
        flash('You were logged in')
        return redirect(url_for('listar'))

    return render_template('formulario.html', error=error)


if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.debug = True
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
