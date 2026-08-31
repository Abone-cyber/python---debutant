def dire_bonjour(nom):
    return f"Bonjour {nom} !"

def additionner(a, b):
    return a + b

def carre(nombre):
    return nombre ** 2

# if __name__ == "__main__": sert à tester du code(fonctions et autres) destiné à etre utilisé dans d'autres fichiers.
if __name__ == "__main__":
    print(dire_bonjour("Alice"))
    print(additionner(10, 5))
    print(carre(5))

# Le code ci-dessus s'excécute uniquement si on le lance ici.

# Dans main.py , il ne s'excécute pas car en faisant [import mon_modle],
# name devient mon_module et le if devient faux. D'où la non-excécution.

#Voici un court aperçu du fichier main.py que j'ai supprimé car inutile.----->
#  import mon_module

#print(mon_module.carre(5))