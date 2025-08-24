class Inventaire:
    def __init__(self):
        self.objets = []
    
    def ajouter_objet(self,objet):
        self.objets.append(objet)

    def afficher_objet(self):
        if self.objets:
            print("Inventaire : ", ", ".join(self.objets))
        else:
            print("Inventaire vide.")
        
class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.inventaire = Inventaire()
    
    def ajouter_objet_inventaire(self, objet):
        self.inventaire.ajouter_objet(objet)


    def afficher_inventaire(self):
        print(f"Inventaire de {self.nom} : ")
        self.inventaire.afficher_objet()

class Jeu:
    def __init__(self):
        self.joueurs = []
    
    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def trouver_joueur(self, nom):
        for joueur in self.joueurs:
            if joueur.nom == nom:
                return joueur
        return None
    def afficher_joueurs(self):
        print("Liste des joueurs : ")
        for joueur in self.joueurs:
            print("-", joueur.nom)
    
if __name__ == "__main__":
    
    jeu = Jeu()

    while True:
        print("\n== MENU  ===")
        print("1. Ajouter un joueur")
        print("2. Ajouter un objet à un joueur")
        print("3. Afficher la liste des joueurs")
        print("4. Afficher l'inventaire d'un joueur")
        print("5. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            nom = input("Nom du joueur : ")
            jeu.ajouter_joueur(nom)
            print(f"Joueur {nom} ajouté avec succès !")
        elif choix == "2":
            nom = input("Nom du joueur : ")
            joueur = jeu.trouver_joueur(nom)
            if joueur:
                objet = input("Nom de l'objet : ")
                joueur.ajouter_objet_inventaire(objet)
                print(f"Objet {objet} ajouté à {nom}.")
            else:
                print("Joueur introuvable.")
        elif choix == "3":
            jeu.afficher_joueurs()
        elif choix == "4":
            nom = input("Nom du joueur :")
            jeu.trouver_joueur(nom)
            if joueur:
                joueur.afficher_inventaire()
            else:
                print("Joueur introuvable.")
        elif choix == "5":
            print("Merci d'avoir joué !")
            break
        else:
            print("Choix invalide. Essayez encore.")