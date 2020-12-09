try:
	with open("depart.txt",'r') as pointer:
		content=pointer.read()
except FileNotFoundError:
	print("depart file not found")
try:
	with open("arrivee.txt",'a') as ariveepointer:
		ariveepointer.write(content)
except FileNotFoundError:
	print("arrived file not found")
