from Tkinter import *
import Tkinter
import tkMessageBox

top = Tk()
# text = Text(top)
# text.insert(INSERT, "Hello.....")
# text.insert(END, "Bye Bye.....")
var = StringVar()
label = Label(top, textvariable=var, relief=RAISED)
var.set("hello")


def janelaResposta():
    tkMessageBox.showinfo("resposta")


B = Button(label, text="clique aqui", command=janelaResposta())
B.pack

label.pack()
label.mainloop()
