class Professeur:
    def __init__(self, nom):
        self.nom = nom

    def afficher(self):
        return self.nom
    
prof1 = Professeur("Alice")
prof2 = Professeur("Bob")

class Ecole:
    def __init__(self, nom):
        self.nom = nom
        self.professeurs = []

    def ajouter_professeur(self, professeur):
        self.professeurs.append(professeur)

    def afficher_professeurs(self):
        for professeur in self.professeurs:
            print(professeur.afficher())

ecole = Ecole("Lycée Python")

ecole.ajouter_professeur(prof1)
ecole.ajouter_professeur(prof2)

ecole.afficher_professeurs()