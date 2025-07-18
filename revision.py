def analyse_nombre(n):
    n = int(input("Entrez un nombre : "))
    if n % 2 == 0:
        print("Votre nombre est paire.\n")
    else:
        print("Votre nombre est impair.\n")
    print("le carre de votre nombre est : ", str(n * n) + "\n")
    

def enregistrer_utilisateur(nom):
    nom = print("Quel est votre nom ?")
    with open("utilisateurs.txt", "w") as f:
         f.write(nom)
    with open("utilisateurs.txt", "r") as f:
        contenue = f.read()
    print(contenue)
    
def menu(x):
    x = int(input("Tapez 1 pour analyser un nombre. Tapez 2 pour enregistrer un utilisateur."))
    if x == 1:
        analyse_nombre()
    elif x == 2:
        enregistrer_utilisateur()
    menu(x)
