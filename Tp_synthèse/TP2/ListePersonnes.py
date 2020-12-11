class ListePersonne:
	#constructeur
	def __init__(self,Personne):
		self._Personne = []
		@property
	def Personne(self):
		return self._Personne

	@Personne.setter
	def Personne(self,v):
		self._Personne = v
	def __str__(self):
		return "{}".format(self._Personne)



def exists_code_postal(self,cp):
		if cp in self._adresse:
			return true
		else:
			return 'False'