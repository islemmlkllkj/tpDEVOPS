# Ma classe
class Adresse:
	def __init__(self,rue, numero,code_postal,ville):
		assert len(rue) > 3 and len(rue) < 25, "la rue doit contenir entre 3 et 25 caractères"
		self.rue = rue
		self.numero = numero
		self.code_postal = code_postal
		self.ville = ville
	#redefinition de la méthode d'affichage
	def __str__(self):
		return "{} \n{}\n{}\n{}".format(self.rue,self.numero,self.code_postal,self.ville)
#Mère
class Personne:
	def __init__(self,nom,prenom,age):
		self.nom = nom
		self.prenom = prenom
		self.age = age
	#redefinition de la méthode d'affichage
	def __str__(self):
		return "{} \n{}\n{}\n{}".format(self.nom,self.prenom,self.age)
		
#Classe Fille
class Etudiant(Personne):
	def __init__(self,nom,prenom,age,moyenne):
		Personne.__init__(self,nom,prenom,age)
		self.moyenne = moyenne
#Classe Fille
class Professeur(Personne):
	def __init__(self,nom,prenom,age,matiere_enseignee):
		Personne.__init__(self,nom,prenom,age)
		self.matiere = matiere_enseignee

# Programme principal
a1 = Adresse("rue de paris","5","75000","Paris")
print(a1)