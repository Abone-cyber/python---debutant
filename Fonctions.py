def bonjour_nom(nom):
    print("bonjour", nom)
bonjour_nom("[nom] !")

a = int(input("Entrez un nombre "))
def carre(a):
    return a * a
resultat = carre(a)
print(resultat)

n = int(input("entrez un nombre "))
def parite(n):
    if n % 2 == 0:
        print(n, " est pair.")
    else:
        print(n, "est impair.")
parite(n)
