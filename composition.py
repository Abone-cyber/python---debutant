class Moteur:
    def __init__(self, puissance):
        self.puissance = puissance


class Voiture:
    def __init__(self, marque) :
        self.marque = marque
        self.moteur = Moteur(150)

voiture = Voiture("Toyota")

print(voiture.moteur.puissance)

voiture.moteur.puissance = 200
print(voiture.moteur.puissance)

voiture1 = Voiture("Toyota")
voiture2 = Voiture("BMW")

voiture1.moteur.puissance = 300

print(voiture1.moteur.puissance)  
print(voiture2.moteur.puissance)  