try:
    n = int(input("Entrez un nombre : "))
    print(n / 100)
except ValueError:
    print("Veuillez entre un nombre entier.")
except ZeroDivisionError:
    print("La division par zéro est impossible.")
finally:
    print("Fin du programme.")