from cookielib import reach

from flask import *
import os
from werkzeug.utils import *

from flask import Blueprint
from pip._vendor.pyparsing import empty

from negocio import anotacao

modulo1 = Blueprint('modulo1', __name__,
                    template_folder='templates')

from negocio.anotacao import *
from negocio.usuario import *
from negocio.imagem import *

from negocio.relacionamento_usuarioanotacao import *
import datetime


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@modulo1.route("/session", methods=['POST'])
def login():
    error = None
    # usuarioDAO = UsuarioDAO()
    # print Usuario.query(func.count(Usuario.nome==request.form['username'], Usuario.senha==request.form['password']))

    registered_user = Usuario.query.filter(Usuario.nome == request.form['username'], Usuario.senha == request.form[
        'password']).first()

    if registered_user is None:
        flash('Username or Password is invalid', 'error')
        return redirect(url_for('login'))
    else:
        session['user_id'] = registered_user.id
        # print session['user_id']
        session['user'] = registered_user.nome
        # print session['user']
        session['logged_in'] = True
        flash('You were logged in')
        return redirect(url_for('modulo1.listar'))


@modulo1.route('/logout')
def logout():
    # session.pop('user', session.get('user'))
    session.pop('user')
    session.pop('user', session.get('user'))
    session.pop('logged_in', None)
    # anotacaoDAO = AnotacaoDAO()
    # lista = anotacaoDAO.listar()
    return redirect(url_for('admin.index'))
    # return render_template("listarAnotacaofree.html", lista=lista)


@modulo1.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']


@modulo1.route("/listar")
def listar(name=None, mensagem=None):
    if g.user:

        # anotacaoDAO = AnotacaoDAO()
        # lista = anotacaoDAO.listar()

        lista = Anotacao.query.join(relacionamento_usuarioanotacao,
                                    (relacionamento_usuarioanotacao.c.anotacao_id == Anotacao.id)).filter(
            relacionamento_usuarioanotacao.c.usuario_id == session.get('user_id')).filter(
            Anotacao.lixeira == False).order_by(Anotacao.data)

        # lista = Anotacao.query.filter(Anotacao.lixeira == False).order_by(Anotacao.data)
        return render_template("listarAnotacao.html", name=session.get('user'), lista=lista, mensagem=mensagem,
                               tipo='lista')
    else:
        # return render_template("formulario_login.html")
        return redirect(url_for('login'))


@modulo1.route("/listarLixeira")
def listarLixeira(name=None, mensagem=None):
    if g.user:
        # anotacaoDAO = AnotacaoDAO()
        # lista = anotacaoDAO.listar_lixeira()
        lista = Anotacao.query.join(relacionamento_usuarioanotacao,
                                    (relacionamento_usuarioanotacao.c.anotacao_id == Anotacao.id)).filter(
            relacionamento_usuarioanotacao.c.usuario_id == session.get('user_id')).filter(
            Anotacao.lixeira == True).order_by(Anotacao.data)
        # lista = Anotacao.query.filter(Anotacao.lixeira == True).order_by(Anotacao.data)
        return render_template("listarLixeira.html", name=session.get('user'), lista=lista, mensagem=mensagem,
                               tipo='lixeira')
    else:
        # return render_template("formulario.html")
        return redirect(url_for('login'))


@limiter.limit("1 per 10 seconds")
@modulo1.route("/formularioAnotacao")
def formularioAnotacao(error=None):
    if g.user:
        return render_template("adicionarAnotacao.html", error=error)
    else:
        # return render_template("formulario.html")
        return redirect(url_for('login'))


@limiter.limit("1 per 10 seconds")
@modulo1.route("/adicionarAnotacao", methods=['POST'])
def adicionar(tituloAnotacao=None, descricaoAnotacao=None):
    if g.user:
        error = None
        if request.form['tituloAnotacao'] != empty:
            if request.form['descricaoAnotacao'] != empty:
                anotacao = None
                filename = None
                usuario = Usuario.query.filter(Usuario.id == session.get('user_id')).first()
                file = request.files['file']
                if 'file' not in request.files:
                    # anotacaoDAO = AnotacaoDAO()  # anotacaoDAO.inserir(anotacao)

                    anotacao = Anotacao(None, request.form['tituloAnotacao'], request.form['descricaoAnotacao'],
                                        datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
                    usuario.addAnotacao(anotacao)

                if file.filename == '':
                    anotacao = Anotacao(None, request.form['tituloAnotacao'], request.form['descricaoAnotacao'],
                                        datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
                    usuario.addAnotacao(anotacao)

                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    anotacao = Anotacao(None, request.form['tituloAnotacao'], request.form['descricaoAnotacao'],
                                        datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))

                    usuario.addAnotacao(anotacao)
                    anotacao = Anotacao.query.order_by(Anotacao.id.desc()).first()
                    anotacao.addImagem(filename)

                mensagem = 'anotacao inserida'

                return redirect(url_for('modulo1.listar', name=session.get('user'), mensagem=mensagem))
            else:
                error = "descricao vazia"
                return redirect(url_for('modulo1.formularioAnotacao', error=error))
        else:
            error = "titulo vazio"
            return redirect(url_for('modulo1.formularioAnotacao', error=error))

    else:
        return render_template("formulario_login.html")


@modulo1.route("/deletaimagem", methods=['GET'])
def deletaimagem():
    print request.args.get('idhiddenimagem')
    imagem = Imagem.query.filter(Imagem.id == request.args.get('idhiddenimagem')).first()
    imagem.deleteImagem()
    return redirect(url_for('modulo1.listar', name=session.get('user'), mensagem='imagem deletada'))


@modulo1.route("/acao", methods=['POST'])
def manipula():
    if g.user:
        # anotacaoDAO = AnotacaoDAO()
        url = 'modulo1.listar'
        mensagem = None
        if request.form['funcao'] == 'Deletar':
            # anotacaoDAO.excluir(request.form['button'])
            Anotacao.query.filter(Anotacao.id == request.form['idhidden']).update({'lixeira': True})
            db.session.commit()
            mensagem = "deletado"
        elif request.form['funcao'] == 'Alterar':
            if request.form['alteracao'] == 'ok':
                # anotacaoDAO.update(request.form['id'], request.form['titulo'], request.form['descricao'],request.form['data'])

                Anotacao.query.filter(Anotacao.id == request.form['idhidden']).update(
                    {'titulo': request.form['titulo'], 'descricao': request.form['descricao'],
                     'data': datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')})

                db.session.commit()
                mensagem = "alterado"
            else:
                return render_template("alterarAnotacao.html",
                                       anotacao=Anotacao.query.filter(Anotacao.id == request.form['idhidden']).first())
        elif request.form['funcao'] == 'Deletar Permanentemente':
            # anotacaoDAO.excluir_permanentemente(request.form['button'])
            anotacao = Anotacao.query.filter(Anotacao.id == request.form['idhidden']).first()
            anotacao.deletarAnotacao()
            # db.session.delete(anotacao)
            # db.session.commit()
            mensagem = "deletado permanentemente"
            url = 'modulo1.listarLixeira'
        elif request.form['funcao'] == 'Restaurar':
            # anotacaoDAO.restaurar(request.form['button'])
            Anotacao.query.filter(Anotacao.id == request.form['idhidden']).update({'lixeira': False})
            db.session.commit()
            mensagem = "restaurado"
            url = 'modulo1.listarLixeira'
        elif request.form['funcao'] == 'Adicionar mais imagens':
            if request.form['alteracao'] == 'ok':
                # anotacaoDAO.update(request.form['id'], request.form['titulo'], request.form['descricao'],request.form['data'])
                # 'imagem': request.form['imagem']
                file = request.files['file']
                if 'file' not in request.files:
                    mensagem = "sem imagem"
                if file.filename == '':
                    mensagem = "sem imagem"
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    anotacao = Anotacao(request.form['idhidden'])
                    anotacao.addImagem(filename)
                    mensagem = "alterado"
            else:
                return render_template("adicionarImagens.html",
                                       anotacao=Anotacao.query.filter(Anotacao.id == request.form['idhidden']).first())
        elif request.form['funcao'] == 'Deletar Imagem':
            imagem = Imagem.query.filter(Imagem.id == request.form['idhiddenimagem']).first()
            imagem.deleteImagem()
            # db.session.delete(imagem)
            # db.session.commit()
            mensagem = "imagem deletada"
        elif request.form['funcao'] == 'Compartilhar':
            if request.form['alteracao'] == 'ok':

                usuario = Usuario.query.filter(Usuario.id == request.form['idhiddenusuario']).first()
                anotacao = Anotacao.query.filter(Anotacao.id == request.form['idhiddenanotacao']).first()
                usuario.addAnotacao(anotacao)
                mensagem = "alterado"
            else:

                return render_template("listarUsuarios.html", tipo='compartilhamento', name=session.get('user'),
                                       lista=Usuario.query.filter(Usuario.id != session.get('user_id')),
                                       anotacao=Anotacao.query.filter(Anotacao.id == request.form['idhidden']).first(),
                                       butao='Compartilhar')
        elif request.form['funcao'] == 'Desfazer compartilhamento':
            if request.form['alteracao'] == 'ok':
                usuario = Usuario.query.filter(Usuario.id == request.form['idhiddenusuario']).first()
                anotacao = Anotacao.query.filter(Anotacao.id == request.form['idhiddenanotacao']).first()
                usuario.deleteAnotacao(anotacao)
                if Anotacao.query.join(relacionamento_usuarioanotacao,
                                       (relacionamento_usuarioanotacao.c.anotacao_id == Anotacao.id)).filter(
                            relacionamento_usuarioanotacao.c.anotacao_id == anotacao.id).count() == 0:
                    Anotacao.deletarAnotacao(anotacao)
                mensagem = "removido"
            else:
                return render_template("listarUsuarios.html", tipo='Desfazer compartilhamento',
                                       name=session.get('user'),
                                       lista=Usuario.query.join(relacionamento_usuarioanotacao, (
                                           relacionamento_usuarioanotacao.c.usuario_id == Usuario.id)).filter(
                                           relacionamento_usuarioanotacao.c.anotacao_id == request.form['idhidden']),
                                       anotacao=Anotacao.query.filter(Anotacao.id == request.form['idhidden']).first(),
                                       butao='Desfazer compartilhamento')

        else:
            mensagem = "nao deu"
        return redirect(url_for(url, name=session.get('user'), mensagem=mensagem))

    else:
        return render_template("formulario_login.html")


@modulo1.route("/novafuncao")
def novafuncao():
    return redirect(url_for('modulo1.listar', name=session.get('user'), mensagem='imagem deletada'))


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
