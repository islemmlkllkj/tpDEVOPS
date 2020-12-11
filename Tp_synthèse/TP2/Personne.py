class Personne:
	#constructeur
	def __init__(self,nom,sexe,adresse):
		self._nom = nom
		self._sexe = sexe
		self._adresse = adresse
	#redefinition de la méthode d'affichage
	@property
	def nom(self):
		return self._nom
	@nom.setter
	def nom(self,p):
		self._nom = p

	@property
	def sexe(self):
		return self._sexe
	@sexe.setter
	def sexe(self,n):
		self._sexe = n

	@property
	def adresse(self):
		return self._adresse

	@adresse.setter
	def adresse(self,p):
		self._adresse = p

	def __str__(self):
		return "l adresse de {} {} est {}".format(self._sexe,self._nom,self._adresse)


def find_by_nom(self,s):
		if s in self._nom:
			return self._adresse
		else:
			return 'NULL'


