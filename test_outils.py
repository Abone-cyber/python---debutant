import outils
n  = int(input("Veuillez entrer un nombre : "))
print("Le carré de votre nombre est:", outils.carre(n))

if outils.est_pair(n):
    print("Votre nombre est pair.")
else:
    print("Votre nombre est impair.")
