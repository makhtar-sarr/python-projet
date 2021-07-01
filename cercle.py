from math import*
from point import*

class Cercle(Point):
    # Constructeur d'un Cercle
    def __init__(self, x, y, rayon):
        Point.__init__(self, x, y)
        self.rayon = rayon

    # Calcul du perimetre
    def getPerimetre(self):
        return 2*self.rayon*pi

    # Calcul surface
    def getSurface(self):
        return self.rayon**2*pi
    
    # Appartenance
    def appartient(self, p):
        return self.rayon == sqrt((p.x - self.x)**2 + (p.y - self.y))
    
    # Affichage du cercle
    def afficher(self):
        print("(",self.x,", ",self.y,",",self.rayon,")")
