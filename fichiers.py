with open("utilisateurs.txt", "w") as f:
    f.write("Nelson\n")
    f.write("Mandela\n")
    f.write("Junior\n")

with open("utilisateurs.txt", "r") as f:
    for n in f:
     print("Bonjour", n)

nom = input("Veuillez saisir un nom à ajouter dans la liste : ")

with open("utilisateurs.txt", "a") as f:
    f.write(nom + "\n")

with open("utilisateurs.txt", "r") as f:
        contenue = f.read()
        print(contenue)