#coding:utf-8

print("Qu'est ce que vous voulez faire ?")
operation = str(input())
if(operation=="€"): #si conversion euro --> dollar
	print("entrer le montant en euro")
	euro = int(input())
	dollar = euro * 1.42408
	print("le monatant {} euro en dollar est :{} dollar".format(euro, dollar))
elif(operation=="$"): #si conversion euro --> dollar
	print("entrer le montant en dollar")
	dollar = int(input())
	euro = dollar * 91/100 
	print("le monatant {} dollar en euro est :{} euro".format(dollar, euro))