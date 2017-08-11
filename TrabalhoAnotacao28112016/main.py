# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
from negocio.usuario import *
from persistencia import *


root = Tk()
menubar = Menu(root)

def testeNumero(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    try:
        print root.Lb1.curselection()[0]
    except:
        print root.Lb1.get(root.Lb2.curselection()[0])
    button.pack()


def cadastrarCliente():
    filewin = Toplevel(root)
    filewin.L1 = Label(filewin, text="Digite o nome do cliente:")
    filewin.E1 = Entry(filewin, bd=1)
    filewin.L2 = Label(filewin, text="Digite a renda do cliente:")
    filewin.E2 = Entry(filewin, bd=1)
    button = Button(filewin, text="Cadastrar Cliente", command=lambda:buttonCadastrarCliente(filewin.E1.get(),filewin.E2.get(),filewin))
    filewin.L1.pack()
    filewin.E1.pack()
    filewin.L2.pack()
    filewin.E2.pack()
    button.pack()

def buttonCadastrarAnotacao(nome,renda,win):
    if nome and not nome.isspace():
        if (testeNumero(renda)):
            root.dao.cadastrarCliente(Cliente(0,nome,renda))
            root.Lb1.insert(END, nome)
            root.Lb1.update_idletasks()
            root.Lb2.insert(END, renda)
            root.Lb2.update_idletasks()
            root.Lb1.select_set(0)  # This only sets focus on the first item.
            root.Lb1.event_generate("<<ListboxSelect>>")
            root.vet = root.dao.listarClientes()
            win.destroy()

def deletarCliente():
    filewin = Toplevel(root)
    try:
        index = root.Lb1.curselection()[0]
    except:
        index = root.Lb2.curselection()[0]

    cliente = root.vet[index]
    filewin.L1 = Label(filewin, text="Tem certeza que deseja deletar o cliente %s?" % (cliente.nome))
    filewin.L1.grid(row=0, column=0,columnspan=2)
    cancelar = Button(filewin, text="Cancelar", command=filewin.destroy)
    deletar = Button(filewin, text="Deletar", command=lambda:buttonDeletarCliente(cliente,index,filewin))
    cancelar.grid(row=1, column=0)
    deletar.grid(row=1, column=1)

def buttonDeletarCliente(cliente,index,win):
    root.dao.deletarCliente(cliente)
    root.Lb1.delete(index)
    root.Lb1.update_idletasks()
    root.Lb2.delete(index)
    root.Lb2.update_idletasks()
    root.Lb1.select_set(0)  # This only sets focus on the first item.
    root.Lb1.event_generate("<<ListboxSelect>>")
    win.destroy()




def listarDependentes():
    filewin = Toplevel(root)
    try:
        index = root.Lb1.curselection()[0]
    except:
        index = root.Lb2.curselection()[0]

    cliente = root.vet[index]

    filewin.vet = root.dao.listarDependentesCliente(cliente)

    filewin.Lb1 = Listbox(filewin, width=25)
    filewin.L1 = Label(filewin, text="Dependentes:")
    filewin.Lb2 = Listbox(filewin, width=25)
    filewin.L2 = Label(filewin, text="Idade:")
    for row in filewin.vet:
        filewin.Lb1.insert(END, row.nome)
        filewin.Lb2.insert(END, row.idade)
    filewin.Lb1.select_set(0)  # This only sets focus on the first item.
    filewin.Lb1.event_generate("<<ListboxSelect>>")

    filewin.L1.grid(row=0, column=0)
    filewin.Lb1.grid(row=1, column=0)
    filewin.L2.grid(row=0, column=1)
    filewin.Lb2.grid(row=1, column=1)
    atualizar = Button(filewin, text="Atualizar Dependente", command=lambda:atualizarDependente(filewin.vet[filewin.Lb1.curselection()[0]],filewin))
    atualizar.grid(row=2, column=0)
    deletar = Button(filewin, text="Deletar Dependente", command=lambda:deletarDependente(filewin.vet[filewin.Lb1.curselection()[0]],filewin))
    deletar.grid(row=2, column=1)


menubar.add_cascade(label="Cliente", menu=clientemenu)

root.Lb1 = Listbox(root,width=25)
root.L1 = Label(root, text="Clientes:")
root.Lb2 = Listbox(root,width=25)
root.L2 = Label(root, text="Renda:")


root.vet = root.dao.listarClientes()
for row in root.vet:
    root.Lb1.insert(END, row.nome)
    root.Lb2.insert(END, row.renda)

root.L1.grid(row=0, column=0)
root.Lb1.grid(row=1,column=0)
root.L2.grid(row=0, column=1)
root.Lb2.grid(row=1,column=1)
root.Lb1.select_set(0)  # This only sets focus on the first item.
root.Lb1.event_generate("<<ListboxSelect>>")

def cadastrarDependente():
    filewin = Toplevel(root)
    try:
        index = root.Lb1.curselection()[0]
    except:
        index = root.Lb2.curselection()[0]

    cliente = root.vet[index]

    filewin.L0 = Label(filewin, text="Cliente: %s" % (cliente.nome))
    filewin.L1 = Label(filewin, text="Digite o nome do dependente:")
    filewin.E1 = Entry(filewin, bd=1)
    filewin.L2 = Label(filewin, text="Digite a idade do dependente:")
    filewin.E2 = Entry(filewin, bd=1)
    button = Button(filewin, text="Cadastrar Dependente", command=lambda:buttonCadastrarDependente(filewin.E1.get(),filewin.E2.get(),filewin,cliente))
    filewin.L0.pack()
    filewin.L1.pack()
    filewin.E1.pack()
    filewin.L2.pack()
    filewin.E2.pack()
    button.pack()

def buttonCadastrarDependente(nome,idade,win,cliente):
    if nome and not nome.isspace():
        if (testeNumero(idade)):
            root.dao.cadastrarDependente(Dependente(0,cliente.id,nome,idade))
            root.Lb1.select_set(0)  # This only sets focus on the first item.
            root.Lb1.event_generate("<<ListboxSelect>>")
            win.destroy()
        else:
            print 'erro'

def deletarDependente(dependente,filewin):
    deletewin = Toplevel(root)

    deletewin.L1 = Label(deletewin, text="Tem certeza que deseja deletar o dependente %s?" % (dependente.nome))
    deletewin.L1.grid(row=0, column=0,columnspan=2)
    cancelar = Button(deletewin, text="Cancelar", command=deletewin.destroy)
    deletar = Button(deletewin, text="Deletar", command=lambda:buttonDeletarDependente(dependente,filewin,deletewin))

    cancelar.grid(row=1, column=0)
    deletar.grid(row=1, column=1)

def buttonDeletarDependente(dependente,win1,win2):
    root.dao.deletarDependente(dependente)
    win1.destroy()
    win2.destroy()

def atualizarDependente(dependente,filewin):
    atualwin = Toplevel(filewin)

    atualwin.L1 = Label(atualwin, text="Nome:")
    atualwin.E1 = Entry(atualwin, bd=1)
    atualwin.E1.insert(0,dependente.nome)
    atualwin.L2 = Label(atualwin, text="Idade:")
    atualwin.E2 = Entry(atualwin, bd=1)
    atualwin.E2.insert(0,dependente.idade)
    button = Button(atualwin, text="Atualizar Dependente", command=lambda:buttonAtualizarDependente(dependente.id,atualwin.E1.get(),atualwin.E2.get(),atualwin,filewin))
    atualwin.L1.pack()
    atualwin.E1.pack()
    atualwin.L2.pack()
    atualwin.E2.pack()
    button.pack()

def buttonAtualizarDependente(id, nome,idade,win,win2):
    if nome and not nome.isspace():
        if (testeNumero(idade)):
            root.dao.atualizarDependente(Dependente(id,0,nome,idade))
            root.Lb1.select_set(0)  # This only sets focus on the first item.
            root.Lb1.event_generate("<<ListboxSelect>>")

            win.destroy()
            win2.destroy()

dependentemenu = Menu(menubar, tearoff=0)
dependentemenu.add_command(label="Mostrar Dependentes", command=listarDependentes)
dependentemenu.add_separator()
dependentemenu.add_command(label="Cadastrar Dependente", command=cadastrarDependente)
menubar.add_cascade(label="Dependente", menu=dependentemenu)





root.config(menu=menubar)
root.mainloop()