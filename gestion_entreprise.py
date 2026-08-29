class Employe:
    def __init__(self, nom, salaire, ordinateur):
        self.__nom = nom
        self.__salaire = salaire
        self.ordinateur = ordinateur

    def afficher_infos(self):
        return f"Nom : {self.__nom} | Salaire : {self.__salaire} FCFA"
    
class Developpeur(Employe):
    def __init__(self, nom, salaire, langage, ordinateur):
        super().__init__(nom, salaire,ordinateur)
        
        self.langage = langage

    def afficher_infos(self):
        return super().afficher_infos() + f" | Langage : {self.langage}"
    
class Designer(Employe):
    def __init__(self, nom, salaire, outil, ordinateur):
        super().__init__(nom, salaire,ordinateur)

        self.outil = outil

    def afficher_infos(self):
        return super().afficher_infos() + f" | Outil : {self.outil}"

class Processeur:
    def __init__(self, modele, frequence):
        self.modele = modele
        self.frequence = frequence
    
class Ordinateur:
    def __init__(self, marque):
        self.marque = marque
        self.processeur = Processeur("Intel", "2,5 GHz")

pc = Ordinateur("Dell")

dev = Developpeur("Alice", 400000, "Python", pc)

print(dev.ordinateur.marque)


