from sqlite3 import *
connection = connect("GestionFormation.db")
cursor = connection.cursor()

#ajout
def AjouterMatiere():
	new_matiere = (cursor.lastrowid,'java')
	cursor.execute('INSERT INTO Matiere VALUES(?,?)',new_matiere)
	connection.commit()
	pass

def AjouterCursus():
	new_Cursus = (cursor.lastrowid,'Developpeur C#')
	cursor.execute('INSERT INTO Cursus VALUES(?,?)',new_Cursus)
	connection.commit()
	pass


def AjouterEtudiant():
	new_etudiant = (cursor.lastrowid,"tDDD","taSDD",25,2)
	cursor.execute('INSERT INTO etudiant VALUES(?,?,?,?,?)',new_etudiant)
	connection.commit()
	pass


#lister
def ListerMatiere():
	cursor.execute('SELECT * FROM Matiere')
	print(cursor.fetchall())
	pass
def ListerCursus():
	cursor.execute('SELECT * FROM cursus')
	print(cursor.fetchall())
	pass
def ListerEtudiant():
	cursor.execute('SELECT * FROM etudiant')
	print(cursor.fetchall())
	pass
#modifier
def ModifierMatiere():
	new_matiere=('C#',1)
	cursor.execute('UPDATE Matiere SET nomMatiere=? WHERE idMatiere=?',new_matiere)
	connection.commit()
	pass
def ModifierCursus():
	new_Cursus=('Devops',1)
	cursor.execute('UPDATE Cursus SET nomCursus=? WHERE idCursus=?',new_matiere)
	connection.commit()
	pass
def ModifierEtudiant():
	mon_etudiant=('hugo','lsls',25,5)
	cursor.execute('UPDATE Etudiant SET nomEtudiant=?, prenomEtudiant=?, age=? WHERE idEtudiant=?',mon_etudiant)
	connection.commit()
	pass
#delete
def DeleteMatiere():
	del_Matiere=(8,)
	cursor.execute('Delete from Matiere WHERE idMatiere=?',del_Matiere)
	connection.commit()
	pass
def DelateCursus():
	del_Cursus=(3,)
	cursor.execute('Delete from Cursus WHERE idCursus=?',del_Cursus)
	connection.commit()
	pass
def DelateEtudiant():
	del_etudiant=(3,)
	cursor.execute('Delete from Etudiant WHERE idEtudiant=?',del_etudiant)
	connection.commit()
	pass

def afficherEtudiantDeCursus():
	idCursus=(2,)
	cursor.execute('SELECT * FROM Etudiant WHERE idcursus=?',idCursus)
	print(cursor.fetchone())
	pass
def afficherMatiereCursus():
	idCursus=(2,)
	cursor.execute('SELECT * FROM Etudiant WHERE idcursus=?',idCursus)
	print(cursor.fetchone())
def afficherCursurs():
	idCursus=(5,)
	cursor.execute('SELECT * FROM Matiere WHERE idCursus=?',idCursus)
	print(cursor.fetchone())
	pass

idMatiere=(6,)
cursor.execute('SELECT * FROM Matiere WHERE idMatiere=?',idMatiere)
print(cursor.fetchone())