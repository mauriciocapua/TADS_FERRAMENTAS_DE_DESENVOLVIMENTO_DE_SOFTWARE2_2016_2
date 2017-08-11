# -*- coding: utf-8 -*-
import tkMessageBox
from Tkinter import *
from negocio.usuario import *
from negocio.anotacao import *
from persistencia.anotacaoDAO import *
from persistencia.usuarioDAO import *

root = Tk()
root.anotacaoDAO = AnotacaoDAO()
root.usuarioDAO = UsuarioDAO()
menubar = Menu(root)


def testeNumero(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def listarUsuarios():
    filewin = Toplevel(root)
    try:
        index = root.Lb1.curselection()[0]
    except:
        index = root.Lb2.curselection()[0]

    usuario = root.vet[index]

    filewin.vet = root.usuarioDAO.listar()

    filewin.Lb1 = Listbox(filewin, width=25)
    filewin.L1 = Label(filewin, text="nome")
    for row in filewin.vet:
        filewin.Lb1.insert(END, row.nome)
        # filewin.Lb2.insert(END, row.descricao)
    filewin.Lb1.select_set(0)  # This only sets focus on the first item.
    filewin.Lb1.event_generate("<<ListboxSelect>>")

    filewin.L1.grid(row=0, column=0)
    filewin.Lb1.grid(row=1, column=0)
    # filewin.L2.grid(row=0, column=1)
    # filewin.Lb2.grid(row=1, column=1)
    atualizar = Button(filewin, text="Atualizar usuario",
                       command=lambda: atualizarusuario(filewin.vet[filewin.Lb1.curselection()[0]], filewin))
    atualizar.grid(row=2, column=0)
    deletar = Button(filewin, text="Deletar usuario",
                     command=lambda: buttonDeletarusuario(filewin.vet[filewin.Lb1.curselection()[0]], filewin,
                                                          filewin.Lb1.curselection()[0]))
    deletar.grid(row=3, column=0)


root.Lb1 = Listbox(root, width=25)
root.L1 = Label(root, text="Usuarios:")

root.vet = root.usuarioDAO.listar()
for row in root.vet:
    root.Lb1.insert(END, row.nome)

root.L1.grid(row=0, column=0)
root.Lb1.grid(row=1, column=0)
root.Lb1.select_set(0)  # This only sets focus on the first item.
root.Lb1.event_generate("<<ListboxSelect>>")


def buttonDeletarusuario(usuario, index):
    root.usuarioDAO.excluir(usuario)
    root.Lb1.delete(index)


def atualizarusuario(usuario, index):
    atualwin = Toplevel(root)

    atualwin.L1 = Label(atualwin, text="nome:")
    atualwin.E1 = Entry(atualwin, bd=1)
    atualwin.E1.insert(0, " ")

    button = Button(atualwin, text="Atualizar usuario",
                    command=lambda: buttonAtualizarusuario(usuario.id, atualwin.E1.get(), atualwin, index))
    atualwin.L1.pack()
    atualwin.E1.pack()
    button.pack()


def buttonAtualizarusuario(id, nome, win, index):
    if nome and not nome.isspace():
        root.usuarioDAO.update(Usuario(id, nome))
        root.Lb1.select_set(0)  # This only sets focus on the first item.
        root.Lb1.event_generate("<<ListboxSelect>>")
        root.Lb1.delete(index)
        root.Lb1.insert(index, nome)
        win.destroy()


def listarAnotacoes():
    filewin = Toplevel(root)
    try:
        index = root.Lb1.curselection()[0]
    except:
        index = root.Lb2.curselection()[0]

    usuario = root.vet[index]

    filewin.vet = root.anotacaoDAO.listar(usuario)

    filewin.Lb1 = Listbox(filewin, width=25)
    filewin.L1 = Label(filewin, text="titulo | descricao")
    # filewin.Lb2 = Listbox(filewin, width=25)
    # filewin.L2 = Label(filewin, text="descricao:")
    for row in filewin.vet:
        filewin.Lb1.insert(END, row.titulo + " | " + row.descricao)
        # filewin.Lb2.insert(END, row.descricao)
    filewin.Lb1.select_set(0)  # This only sets focus on the first item.
    filewin.Lb1.event_generate("<<ListboxSelect>>")

    filewin.L1.grid(row=0, column=0)
    filewin.Lb1.grid(row=1, column=0)
    # filewin.L2.grid(row=0, column=1)
    # filewin.Lb2.grid(row=1, column=1)
    atualizar = Button(filewin, text="Atualizar anotacao",
                       command=lambda: atualizaranotacao(filewin.vet[filewin.Lb1.curselection()[0]], filewin))
    atualizar.grid(row=2, column=0)
    deletar = Button(filewin, text="Deletar anotacao",
                     command=lambda: buttonDeletaranotacao(filewin.vet[filewin.Lb1.curselection()[0]], filewin))
    deletar.grid(row=3, column=0)


root.Lb1 = Listbox(root, width=25)
root.L1 = Label(root, text="Usuarios:")

root.vet = root.usuarioDAO.listar()
for row in root.vet:
    root.Lb1.insert(END, row.nome)

root.L1.grid(row=0, column=0)
root.Lb1.grid(row=1, column=0)
root.Lb1.select_set(0)  # This only sets focus on the first item.
root.Lb1.event_generate("<<ListboxSelect>>")

atualizar = Button(root, text="Atualizar usuario",
                   command=lambda: atualizarusuario(root.vet[root.Lb1.curselection()[0]], root.Lb1.curselection()[0]))
atualizar.grid(row=2, column=0)
deletar = Button(root, text="Deletar usuario",
                 command=lambda: buttonDeletarusuario(root.vet[root.Lb1.curselection()[0]], root.Lb1.curselection()[0]))
deletar.grid(row=3, column=0)


def cadastraranotacao():
    filewin = Toplevel(root)
    try:
        index = root.Lb1.curselection()[0]
    except:
        index = root.Lb2.curselectioxn()[0]

    usuario = root.vet[index]

    filewin.L0 = Label(filewin, text="usuario: %s" % (usuario.nome))
    filewin.L1 = Label(filewin, text="Digite o titulo da anotacao:")
    filewin.E1 = Entry(filewin, bd=1)
    filewin.L2 = Label(filewin, text="Digite a descricao da anotacao:")
    filewin.E2 = Entry(filewin, bd=1)
    button = Button(filewin, text="Cadastrar anotacao",
                    command=lambda: buttonCadastraranotacao(filewin.E1.get(), filewin.E2.get(), filewin, usuario))
    filewin.L0.pack()
    filewin.L1.pack()
    filewin.E1.pack()
    filewin.L2.pack()
    filewin.E2.pack()
    button.pack()


def buttonCadastraranotacao(titulo, descricao, win, usuario):
    if titulo and not titulo.isspace():
        root.anotacaoDAO.inserir(Anotacao(None, titulo, descricao), usuario)
        root.Lb1.select_set(0)  # This only sets focus on the first item.
        root.Lb1.event_generate("<<ListboxSelect>>")
        win.destroy()


def buttonDeletaranotacao(anotacao, win1):
    root.anotacaoDAO.excluir(anotacao)
    win1.destroy()


def atualizaranotacao(anotacao, filewin):
    atualwin = Toplevel(filewin)

    atualwin.L1 = Label(atualwin, text="titulo:")
    atualwin.E1 = Entry(atualwin, bd=1)
    atualwin.E1.insert(0, anotacao.titulo)
    atualwin.L2 = Label(atualwin, text="descricao:")
    atualwin.E2 = Entry(atualwin, bd=1)
    atualwin.E2.insert(0, anotacao.descricao)
    button = Button(atualwin, text="Atualizar anotacao",
                    command=lambda: buttonAtualizaranotacao(anotacao.id, atualwin.E1.get(), atualwin.E2.get(), atualwin,
                                                            filewin))
    atualwin.L1.pack()
    atualwin.E1.pack()
    atualwin.L2.pack()
    atualwin.E2.pack()
    button.pack()


def buttonAtualizaranotacao(id, titulo, descricao, win, win2):
    if titulo and not titulo.isspace():
        root.anotacaoDAO.update(Anotacao(id, titulo, descricao))
        root.Lb1.select_set(0)  # This only sets focus on the first item.
        root.Lb1.event_generate("<<ListboxSelect>>")

        win.destroy()
        win2.destroy()

        root.Lb1.insert(END, row.nome)


def cadastrarUsuario():
    filewin = Toplevel(root)
    try:
        index = root.Lb1.curselection()[0]
    except:
        index = root.Lb2.curselectioxn()[0]

    usuario = root.vet[index]

    filewin.L1 = Label(filewin, text="Digite o nome do usuario:")
    filewin.E1 = Entry(filewin, bd=1)
    button = Button(filewin, text="Cadastrar usuario",
                    command=lambda: buttonCadastrarusuario(filewin.E1.get(), filewin))

    filewin.L1.pack()
    filewin.E1.pack()

    button.pack()


def buttonCadastrarusuario(nome, win):
    if nome and not nome.isspace():
        root.usuarioDAO.inserir(Usuario(None, nome))
        root.Lb1.insert(END, nome)
        root.Lb1.select_set(0)  # This only sets focus on the first item.
        root.Lb1.event_generate("<<ListboxSelect>>")
        win.destroy()


usuariomenu = Menu(menubar, tearoff=0)
usuariomenu.add_command(label="Cadastrar usuarios", command=cadastrarUsuario)
menubar.add_cascade(label="usuario", menu=usuariomenu)

anotacaomenu = Menu(menubar, tearoff=0)
anotacaomenu.add_command(label="Mostrar anotacaos", command=listarAnotacoes)
anotacaomenu.add_separator()
anotacaomenu.add_command(label="Cadastrar anotacao", command=cadastraranotacao)
menubar.add_cascade(label="anotacao", menu=anotacaomenu)

root.config(menu=menubar)
root.mainloop()
