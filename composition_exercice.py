class Processeur:
    def __init__(self, modele, frequence):
        self.modele = modele
        self.frequence = frequence

class Ordinateur:
    def __init__(self, marque):
        self.marque = marque
        self.processeur = Processeur("Intel i5", 2.5)

pc = Ordinateur("Dell")
print(pc.marque)
print(pc.processeur.modele)
print(f"{pc.processeur.frequence} GHz")