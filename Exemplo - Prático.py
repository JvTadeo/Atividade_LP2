
import sqlite3
from tkinter import * 
from tkinter import ttk


root = Tk()

root.title("Sistema de Alunos")
root.geometry('820x600')
my_tree = ttk.Treeview(root)
SystemAln = "SISTEMA DE ALUNOS"

#TITLE 
titleLabel = Label(root, text=SystemAln, font=('Roboto Bold', 30), bd = 1)
titleLabel.grid(row=0, column= 0, columnspan= 8, padx= 10, pady = 10)

#NAME
nameLabel = Label(root, text="NOME DO ALUNO", font=('Roboto', 18), bd = 2)
n1Label = Label(root, text="PRIMEIRA NOTA", font=('Roboto', 18), bd = 1 )
n2Label = Label(root, text="SEGUNDA NOTA", font=('Roboto', 18), bd = 1 )

#ENTRY
nameEntry = Entry(root, width= 40, bd = 3, font =('Roboto', 18))
n1Entry = Entry(root, width= 10, bd = 3, font =('Roboto', 18))
n2Entry = Entry(root, width= 10, bd = 3, font =('Roboto', 18))

#BUTTONS 

buttonEnter = Button(
    root, text="ADICIONAR", padx = 5, pady = 5, width= 10, bd = 2, font=('Roboto', 18), bg="#8ac926"
)

buttonDelete = Button(
    root, text="DELETE", padx = 5, pady = 5, width= 10, bd = 2, font=('Roboto', 18), bg="#ff595e"
)

buttonUpdate = Button(
    root, text="UPDATE", padx = 5, pady = 5, width= 10, bd = 2, font=('Roboto', 18), bg="#ffca3a")



#GRID
nameLabel.grid(row = 1, column= 0, padx = 10, pady = 10, sticky= W)
n1Label.grid(row = 2, column= 0, padx = 10, pady= 10, sticky= W)
n2Label.grid(row = 3, column= 0, padx = 10, pady= 10, sticky= W)
nameEntry.grid(row = 1, column= 1, columnspan= 3, padx= 5, pady= 5, sticky= W)
n1Entry.grid(row = 2, column= 1, columnspan= 3, padx= 5, pady= 5, sticky= W)
n2Entry.grid(row = 3, column= 1, columnspan= 3, padx= 5, pady= 5, sticky= W)

#BUTTONS GRID
buttonEnter.grid(row = 5, column=1, columnspan=1, sticky= W)
buttonUpdate.grid(row = 5, column=2, columnspan=1, sticky= W)
buttonDelete.grid(row = 5, column=3, columnspan=1, sticky= W)


#TABLE CONFIGURATION
style = ttk.Style()
style.configure("Treeview.Heading", font = ('Roboto', 25))

my_tree['columns'] = ("NOME", "PRIMEIRA NOTA", "SEGUNDA NOTA", "MÉDIA")

#COLUMN
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("NOME", anchor=W, width= 120)
my_tree.column("PRIMEIRA NOTA", anchor=W, width= 250)
my_tree.column("SEGUNDA NOTA", anchor=W, width= 250)
my_tree.column("MÉDIA", anchor=W, width= 120)

#HEADING
my_tree.heading("NOME", text="NOME", anchor=W)
my_tree.heading("PRIMEIRA NOTA", text="PRIMEIRA NOTA", anchor=W)
my_tree.heading("SEGUNDA NOTA", text="SEGUNDA NOTA", anchor=W)
my_tree.heading("MÉDIA", text="MÉDIA", anchor=W)


#TAG
my_tree.tag_configure('orow',background='#eaeaea', font=('Roboto', 15))
#GRID
my_tree.grid(row=6, column= 0, columnspan= 4, rowspan= 4, padx= 10, pady= 10)



root.mainloop()