#Base de donnees
from sqlite3 import *
#CRUD : Create ,Read, Update, Delete
#connexion
connection = connect("base.db")
cursor = connection.cursor()
"""
new_etudiant = (cursor.lastrowid,"toto","tata",25)
cursor.execute('INSERT INTO etudiant VALUES(?,?,?,?)',new_etudiant)
connection.commit()

print("le nouvel utilisateur a été ajouté en BD")
#chercher tout les etudiant
cursor.execute('SELECT * FROM etudiant')
print(cursor.fetchall())

#afficher un seul etudiant dont id=3
mon_etudiant=(3,)
cursor.execute('SELECT * FROM etudiant WHERE ID=?',mon_etudiant)
print(cursor.fetchone())
"""
#modifier un utilisateur
"""
mon_etudiant=('modif','djkd',25,1)
cursor.execute('UPDATE etudiant SET nom=?, prenom=?, age=? WHERE ID=?',mon_etudiant)
connection.commit()
"""
mon_etudiant=(3,)
cursor.execute('SELECT * FROM etudiant WHERE ID=?',mon_etudiant)
print(cursor.fetchone())
del_etudiant=(3,)
cursor.execute('Delete from etudiant WHERE ID=?',del_etudiant)
connection.commit()
print("l'etudiant toto est bien supprimé")
mon_etudiant=(3,)
cursor.execute('SELECT * FROM etudiant WHERE ID=?',mon_etudiant)
print(cursor.fetchone())
#fermeture du bdd
cursor.close()
connection.close()