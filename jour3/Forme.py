class Forme:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def calcul_distance(self):
        return('je calcule la distance')
    def calcul_perimetre(self):
        return('je calcule le perimetre')   
    def __init__(self):
        print('je calcule perimetre')

 class Rectangle(Forme):
    def __init__(self,x,y):
        Forme.__init__(self,x,y)

    def Calcul_perimetre(self):
        perimetre = self.x * self.y
        return 'le perimetre est {}'.Format(perimetre)

    def __str__(self):
        print('les coordonnées du rectangle sont {} {}'.Format(self.x,self.y))
        