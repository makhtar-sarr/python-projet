class Point:
    # Constructeur de point
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Affichage d'un point avec print()
    def afficher(self):
        print("(",self.x,", ",self.y,")")
