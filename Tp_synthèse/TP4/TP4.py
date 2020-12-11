import tkinter
from tkinter.messagebox import *

from connection import create_connection
new_conn = create_connection("TP4_Connection.db")
cursor = new_conn.cursor()

def connection ():
	"""
	new_personne = (cursor.lastrowid,'islem','1234k')
	cursor.execute('INSERT INTO Personne VALUES(?,?,?)',new_personne)
	new_conn.commit()
	"""
	cursor.execute('SELECT login FROM Personne')
	rows = cursor.fetchall()
	cursor.execute('SELECT password FROM Personne' )
	rows2 = cursor.fetchall()

	# si le mot correspond à celui attendu
	if var_entry1.get() in rows :
		if var_entry2.get() in rows2:
			showinfo('Résultat','utilisateur connecté')
		else:
			showwarning('Résultat','Mot de passe incorrect.\n erreur de connexion !')
			var_entry2.set('')
	else:
		showwarning('Résultat','login incorrect.\n erreur de connexion  !')
		var_entry1.set('')

#Création de la fenetre globale
root = tkinter.Tk()
#Paramétrer la fenetre globale
root.geometry("400x400")
root.title("TP4: fenetre de connection")
#LabelLogin

w1 = tkinter.Label(root, text = "login")

#Zone de Saisie
var_entry1 = tkinter.StringVar()
entry1 = tkinter.Entry(root,textvariable=var_entry1)

#LabelPassword
w2 = tkinter.Label(root, text = " password")
#Zone de Saisie Password
var_entry2 = tkinter.StringVar()
entry2 = tkinter.Entry(root,textvariable=var_entry2)
# Bouton de connection
bouton = tkinter.Button(root,text='Valider', command=connection)
w1.pack()
entry1.pack()

w2.pack()
entry2.pack()

bouton.pack()
root.mainloop()