#coding:utf-8

list=['Islem','Mannai','2','Devops']
indice = 0
for x in list:
	for y in x:
		indice =  indice  + 1

	print("la chaine {} comporte {} éléments".format(x,indice))
	indice = 0	