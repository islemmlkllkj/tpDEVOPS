#coding:utf-8

#création di dictionnaire
mots={'bonjour':'hello','Moi':'ME','Toi':'You','Amour':'Love','amis':'friends'}
#Ajouter un element au dictionnaire
mots['chat']= 'cat'
#affichage du dictionnaire
print(mots)

#Suppression des element dont leurs clés commance avec 'c'
mots_to_supprimer = [key for key in mots if key.startswith('c')]
for key in mots_to_supprimer: del mots[key]

print("mon dictionnaire après la suppression : \n", mots.values())

	