from modulebdd import *

new_conn = create_connection("GestionFormaton.db")

if new_conn is None:
    raise Exception("Error! cannot create the database connection.")


ajouterMatiere(new_conn,('Java',))
ajouterMatiere(new_conn,('C#',))
ajouterMatiere(new_conn,('Algebre',)

info_id = ajouterCursus(new_conn,('Info',))
math_id = ajouterCursus(new_conn,('Math',))

ajouterEtudiant(new_conn,('nom1','prenom1',20,info_id,))
ajouterEtudiant(new_conn,('nom1','prenom1',20,math_id,))
