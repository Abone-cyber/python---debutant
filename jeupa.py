class Joueur:
    def __init__(self, pseudo, point, niveau):
        self.pseudo = pseudo
        self.point = point
        self.niveau = niveau
        self.inventaire = []
        self.competence = []

    
    @property
    def info_joueur(self):
        return f"Pseudo : {self.pseudo} | Point : {self.point} | Niveau : {self.niveau} | Inventaire : {self.inventaire} | Compétences : {self.competence}"
        

    @info_joueur.setter
    def info_joueur(self, point_only):
        point = point_only

    def resume_info_joueur(self):
        print("\n-"*10 + "INFO DU JOUEUR" + "-"*10)
        print(Joueur.info_joueur)


# Pour ne pas répeter ce message(DRY)
def recompense():
    print("\nBIEN JOUE !!! :) \nVous gagnez 100 points")
    Joueurpoint += 100

class Mission:
    def __init__(self):
        pass
    
    def afficher_missions(self):
        liste_mission = ["Le nombre de compte actif", "Le mot de passe logique"]
        for i, missions in enumerate(liste_mission, start=1):
            print(i, missions)

    def lancer_mission(self):
        Mission.afficher_missions()
        choix = input("\nVous choisissez : ")

        if choix == 1:
            print("MISSION 1")
            print("-"*15)
            print("Un système possède 5 comptes")
            print("\nCompte 1 : actif")
            print("Compte 2: actif")
            print("Compte 3 : bloqué")
            print("Compte 4 : actif")
            print("Compte 5 : bloqué")

        print("Combien de comptes sont actifs ?")
        reponse = input("Votre réponse : ")
        if reponse == 3:
            recompense()
        else:
            print("\nRéponse incorrect :(")

        if choix == 2:
            print("MISSION 02")
            print("-"*15)
            print("Trouve le mot de passe logique :")
            print("\n2 - 4 - 8 - 16 - ?")
            print("\nRéponse :")

            reponse = input("Votre réponse : ")
            if reponse == 32:
                recompense()
            else:
                print("\nRéponse incorrect :(")


        
def jeu(): 
    while True:
        print("="*20)
        print("      CYBER ARENA      ")
        print("="*20)

        print("1 Voir mon profil")
        print("2 Voir les missions")
        print("3 Lancer une mission")
        print("4 Voir mon inventaire")
        print("5 Sauvegarder")
        print("6 Quitter")
        
        choix = str(input("\nVotre choix : "))

        if choix == "1":
            Joueur.resume_info_joueur()
        elif  choix == "2":
            Mission.afficher_missions()
        elif  choix == "3":
            Mission.lancer_mission()
        elif  choix == "4":
            print(Joueur.inventaire)
        else:
            print("Invalid input ! Try again")
            break
jeu()

j = Joueur("Boss", 100, 2)