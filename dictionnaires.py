dico = {
    "Nelson": 10,
    "Mandela": 12,
    "Junior": 14,
    "Kevin": 16,
    "Abraham": 18
}
for n in dico:
    print(n, "a", dico[n], "ans")

nom = input("Veuillez entrez un nom :")
if nom in dico:
    print("Vous avez:" + str(dico[nom]) + " ans.")
else:
    print("Vous n'etes pas enregistré.")
produits = {
        "Phone": 40000,
        "Desktop": 200000,
        "Key": 3000,
        "Microphone": 15000
         }
for p in produits:
    print("A", p, "costs:", produits[p], "FCFA" )
