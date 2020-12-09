#coding:utf-8

number = int(input("Entrer un nombre "))
if(number%2==0):
	print("ce nombre est paire")
elif(number%3==0):
	print("ce nombre est impaire , multiple de 3")
else:
	print("ce nombre est ni paire ni mult de 3")
