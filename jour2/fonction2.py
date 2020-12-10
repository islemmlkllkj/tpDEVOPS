class calculette: 
	def add(a,b):
		return a + b
	def sous(a,b):
		return a - b
	def mult(a,b):
		return a * b
	def div(a,b):
		try:
			return a / b
		except ZeroDivisionError:
			print("saisir un nombre non null")