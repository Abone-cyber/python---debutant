class Joueur:
    def __init__(self, pseudo, point, niveau):
        self.pseudo = pseudo
        self.point = point
        self.niveau = niveau
        self.inventaire = []
        self.competence = []

    @property
    def info_joueur(self):
        return 
        
        with open("bd", "a", encoding="utf-8") as bd:
            bd.write(biblio)


    

class Mission:
    def __init__(self):
      pass  

class Jeu:
    def __init__(self):
        pass 

def menu(): 
    while True:
        print("="*20)
        print("      CYBER ARENA      ")
        print("="*20)

        print("1. Voir mon profil")
        print("2. Voir les missions")
        print("3. Lancer une mission")
        print("4. Voir mon inventaire")
        print("5. Sauvegarder")
        print("6. Quitter")
        
        choix = input("\nVotre choix : ") 

        if choix == 1:
        elif  choix == 2:
        elif  choix == 3:
        elif  choix == 4:
        elif choix == 5:
        elif  choix == 6:
            break
        
        

        biblio = {"Pseudo": self.pseudo,
                  "Point": self.point,
                  "Niveau": self.niveau,
                  "Inventaire": self.inventaire,
                  "Compétence": self.competence}