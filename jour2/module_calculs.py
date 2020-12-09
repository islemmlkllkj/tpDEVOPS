def add(a, b):
    """Méthode pour l'addition"""
    return a + b

def sous(a, b):
    """Méthode pour la soustraction"""
    return  a - b

def mult(a, b):
     """Méthode pour la multiplication"""
     return a * b

def div(a, b):
    """Méthode pour la division"""
    try:
        return a/b
    except ZeroDivisionError:
        print("Veuillez saisir une valeur différente de 0 pour la division")

