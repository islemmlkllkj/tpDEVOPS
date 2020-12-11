class Ville:
	def __init__(self,nomville):
		self.nomville = nomville
		self.listeBat=[]
	def __str__(self):
		return "le nom de la ville est {} comporte {} batiments".format(self.nomville,len(self.listeBat))
	def NombreBatVille(self):
		return len(self.listeBat)
class Batiment:
	def __init__(self,nomBat,nomville):
		self.nomBat = nomBat
		self.nomville=nomville
	def __str__(self):
		return "le batiment est {}se trouve à ".format(self.nomBat,self.nomville)
class Entreprise:
	def __init__(self,nomEntr):
		self.nomEntr = nomEntr
		self.listeBat=[]
		self.listeville=[]
		
	def __str__(self):
		return "le nom de l'entreprise est {}".format(self.nomEntr)
	def NombreBatEntreprise(self):
			return len(self.listeBat)
	def add_ville():
		if ()
		pass
class Employe:
	def __init__(self,nom,prenom,nomBat):
		self.nom = nom
		self.prenom=prenom
		self.nomBat=nomBat
	def __str__(self):
		return "l'employe est {} , {}".format(self.nom, self.prenom)

Entreprise1=Entreprise('ACTIA',[Bat1,Bat2,Bat3])
Ville1=Ville('Paris',[Bat1,Bat2,Bat3])
ville2=Ville('Lyon',[Bat4,Bat5,Bat6])
Batiment1=Batiment('Bat1','Paris')
Batiment2=Batiment('Bat4','Lyon')
Batiment3=Batiment('Bat7','nice')
Employe1=Employe('Paul','nann',Bat1)
Employe2=Employe('tata','titi',Bat2)
Employe3=Employe('mimi','momo',Bat4)
Employe4=Employe('fifi','fofo',Bat2)
Employe5=Employe('sisi','soso',Bat3)
Employe6=Employe('nini','nono',Bat1)
Employe7=Employe('wiwi','wowo',Bat5)
Employe8=Employe('riri','roro',Bat6)
Employe9=Employe('lili','lolo',Bat5)



