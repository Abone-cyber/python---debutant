def ajouter_livre():
    titre = input("Titre du livre : ")
    auteur = input("Auteur : ")
    année = input("Année  : ")

    with open("bibliotheque.txt", "a", encoding="utf-8") as f:
        f.write(f"Titre: {titre} | Auteur: {auteur} | Année: {année}\n")
    print("Livre ajouté avec succès !\n")


def afficher_livres():
    print("\nListe des livres : ")
    with open("bibliotheque.txt", "r", encoding="utf-8") as f:
        contenue = f.read()
        if contenue.strip() == "":
             print("Aucun livre trouvé.")
        else:
             print(contenue)

def rechercher_livre():
    mot_cle = input("Entrez un mot-clé : ").lower()
    trouve = False

    with open("bibliotheque.txt", "r", encoding="utf-8") as f:
         for ligne in f:
              if mot_cle in ligne:
                   print(ligne.strip())
                   trouve = True
    if not trouve:
         print("Pas de livre trouvé.")
         
               

def menu():
   
    while True:
        print("\n========MENU==========")
        print("1. Ajouter un livre")
        print("2. Afficher les livres")
        print("3. Rechercher un livre")
        print("4. Quitter")

        lett_choix = input("\n Entre le numéro de votre choix : ")

        if lett_choix == "1":
                ajouter_livre()
        elif lett_choix == "2":
                afficher_livres()
        elif lett_choix == "3":
             rechercher_livre()
        elif lett_choix == "4":
            break
        else:
            print("Option invalide, veuillez recommencez")
            
menu()
    

