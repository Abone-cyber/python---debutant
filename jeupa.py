class Joueur:
    def __init__(self, pseudo, point, niveau):
        self.pseudo = pseudo
        self.point = point
        self.niveau = niveau
        self.inventaire = []
        self.competence = []

    
    def info_joueur(self):
        return f"Pseudo : {self.pseudo} | Point : {self.point} | Niveau : {self.niveau} | Inventaire : {self.inventaire} | Compétences : {self.competence}"


class Mission:
    def __init__(self):
        pass
    
    def afficher_missions(self):
        liste_mission = ["Le nombre de compte actif", "Le mot de passe logique"]
        print("*"* 10 + "Liste des missions" + "*"* 10)
        for i, missions in enumerate(liste_mission, start=1):
            print(i, missions)

    def lancer_mission(self):
        self.afficher_missions()
        choix = int(input("\nVous choisissez : "))

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
            reponse = int(input("Votre réponse : "))
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

            reponse = int(input("Votre réponse : "))
            if reponse == 32:
                recompense()
            else:
                print("\nRéponse incorrect :(")
        else:
            print("Jeu non-défini pour le moment.")

class Jeu:
    def __init__(self):
        self.liste_joueur = []
    

m = Mission()
j = Joueur("Boss", 0, 2)

def recompense():
    print("\nBIEN JOUE :) \nVous gagnez 100 points")
    j.point += 100

def sauvegarde():
    with open("jeupa.txt", "w", encoding="utf-8") as f:
        f.write(str(j))


def menu(): 
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
        
        choix = int(input("\nVotre choix : "))

        if choix == 1:
            print(j.info_joueur())
        elif  choix == 2:
            m.afficher_missions()
        elif  choix == 3:
            m.lancer_mission()
        elif  choix == 4:
            print(j.inventaire)
        elif choix == 5:
            sauvegarde()
        else:
            print("Invalid input ! Try again")
            break
menu()
