#import du module
from module_calculs import *

#PROGRAMME PRINCIPAL
print("veuillez saisir les informations de calcul")

x=int(input("saisir le premier chiffre:"))
y=int(input("saisir le deuxième chiffre:"))

print("resultat addition :{}".format(add(x,y)))
print("resultat soustraction :{}".format(sous(x,y)))
print("resultat multiplication :{}".format(mult(x,y)))
print("resultat division :{}".format(div(x,y)))