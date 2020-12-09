try:
	valeur1=int(input("donner un entier"))
	assert isinstance(valeur1, (int, float))
	pass
except AssertionError:
	print ("la valeur n'est pas entier")
	raise
try:
	valeur2=int(input("donner un entier"))
	assert isinstance(valeur2, (int, float))
	pass
except AssertionError:
	print ("la valeur n'est pas entier")
	raise
try:
	pair=valeur1 /2 
	div=valeur1 /valeur2
	assert (pair==0)
except AssertionError:
	print ("la valeur n'est pas pair")

try:
	div=valeur1 /valeur2
	assert (valeur2!=0)
except AssertionError:
	print ("la valeur est nulle:Erreur Division par zero!")
print("le resultat de division de {} par {} est égal à {}".format(valeur1,valeur2,div))