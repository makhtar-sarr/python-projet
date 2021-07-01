from cercle import*
class Cylindre(Cercle):
    def __init__(self, x, y, rayon, hauteur):
        Cercle.__init__(self, x, y, rayon)
        self.hauteur = hauteur

    # Surface d'un cylindre
    def getVolume(self):
        return self.getSurface()*self.hauteur