class MontantInvalideError(Exception):
    pass

class SoldeInsuffisantError(Exception):
    pass

class Compte:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.__solde = solde

    @property
    def solde(self):
        return self.__solde
    

    def retirer(self, montant):
        if montant <= 0:
            raise MontantInvalideError("Le montant doit etre superieur à 0.")
        elif montant > self.__solde:
            raise SoldeInsuffisantError("Solde insuffisant.")
        self.__solde -= montant

    def deposer(self, montant):
        if montant <= 0:
            raise MontantInvalideError("Le montant doit etre superieur à 0.")
        self.__solde += montant

    def transferer(self, autre_compte, montant):
        self.retirer(montant)
        autre_compte.deposer(montant)
     
alice = Compte("Alice", 100000)
bob = Compte("Bob", 50000)



try:
    alice.transferer(bob, 30000)
except MontantInvalideError as e:
    print(e)
except SoldeInsuffisantError as e:
    print(e)

print(alice.solde)
print(bob.solde)