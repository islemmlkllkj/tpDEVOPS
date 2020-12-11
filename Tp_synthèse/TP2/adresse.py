class Adresse:
	def __init__(self,rue,codepostal,ville):
		self._rue = rue
		self._codepostal = codepostal
		self._ville = ville

	@property
	def rue(self):
		return self._rue

	@rue.setter
	def rue(self,n):
		self._rue = n
	@property
	def codepostal(self):
		return self._codepostal

	@codepostal.setter
	def codepostal(self,p):
		self._codepostal = p
	@property
	def ville(self):
		return self._ville
	@ville.setter
	def ville(self,k):
		self._ville = k
	def __str__(self):
		return "{} \n{}\n{}\n{}".format(self._rue,self._codepostal,self._ville)




