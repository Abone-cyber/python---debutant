class Employe:
    def __init__(self, nom, salaire, ordinateur):
        self.__nom = nom
        self.__salaire = salaire
        self.ordinateur = ordinateur

    @property
    def nom(self):
        return self.__nom

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

class Entreprise:
    def __init__(self, nom):
        self.nom = nom
        self.employes = []

    def ajouter_employe(self,employe):
        self.employes.append(employe)

    def afficher_employes(self):
        for employe in self.employes:
            print(employe.afficher_infos())

    def rechercher_employe(self, nom):
        for employe in self.employes:
            if nom == employe.nom:
                return employe
        return None

    def supprimer_employe(self, nom):
        for employe in self.employes:
            if nom == employe.nom:
                self.employes.remove(employe)
                return True
        return False



pc = Ordinateur("Dell")

dev = Developpeur("Alice", 400000, "Python", pc)

enterp = Entreprise("CyberTech")
enterp.ajouter_employe(dev)

#Test de recherche d'un employé
employe = enterp.rechercher_employe("Alice")
if employe:
    print(employe.afficher_infos())
else:
    print("Employé introuvable.")

#Test de suppression d'un employé
if enterp.supprimer_employe("Alice"):
    print("Employé supprimé.")
else:
    print("Employé Introuvable.")

enterp.afficher_employes()
print(enterp.supprimer_employe("Alice"))
