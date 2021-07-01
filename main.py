# Import des modules
from point import*
from cercle import*
from cylindre import*

# Teste de la classe Point
print("**** Teste de la classe Point ***")
point1 = Point(4, 0)
point2 = Point(1, 2)
point1.afficher()
point2.afficher()
print()

# Teste de la classe Cercle
print("*** Teste de la classe Cercle ***")
cercle = Cercle(0, 0, 4)
print("Perimetre = ",cercle.getPerimetre())
print("Surface = ",cercle.getSurface())
if cercle.appartient(point1) == True:
    print("Point1 appartient au Cercle ")
else:
    print("Point1 n\'appartient au Cercle ")
if cercle.appartient(point2) == True:
    print("Point2 appartient au Cercle ")
else:
    print("Point2 n\'appartient au Cercle ")
cercle.afficher()
print()

# Teste de la classe Cylindre
cylindre = Cylindre(0, 4, 8, 10)
print("Volume =", cylindre.getVolume())