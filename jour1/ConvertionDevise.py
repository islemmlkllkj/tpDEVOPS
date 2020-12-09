#coding:utf-8

print("Qu'est ce que vous voulez faire ?")
operation = str(input())
if(operation=="€"): #si conversion euro --> dollar
	print("entrer le montant en euro")
	euro = int(input())
	dollar = euro * 1.42408
	print("le monatant en dollar est :{} dollar".format(dollar))
elif(operation=="$"): #si conversion euro --> dollar
	print("entrer le montant en dollar")
	dollar = int(input())
	euro = dollar * 91/100 
	print("le monatant en euro est :{} euro".format(euro))