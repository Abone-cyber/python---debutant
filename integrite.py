from pathlib import Path
import hashlib
import json
dossier = Path(__file__).parent

fichier_empreinte = dossier / "empreintes.json"


def calculer_hash(fichier):
    contenu = fichier.read_bytes()
    hash_obj = hashlib.sha256(contenu)
    return hash_obj.hexdigest()
    

def verifier_integrite(ancienne_empreinte, empreinte):

    resultats = {"ok": [],
                 "modifies": [],                                 
                 "nouveaux": [],
                 "supprimes": []
                 }

    for nom in ancienne_empreinte:
        if nom in empreinte:
            if ancienne_empreinte[nom] == empreinte[nom]:
                resultats["ok"].append(nom)
            else:
                resultats["modifies"].append({
                    "nom": nom,
                    "ancienne": ancienne_empreinte[nom],
                    "nouvelle": empreinte[nom]
                  })
             
    for nom in empreinte:
        if nom not in ancienne_empreinte:
            resultats["nouveaux"].append(nom)

    for nom in ancienne_empreinte:
        if nom not in empreinte:
            resultats["supprimes"].append(nom)
    return resultats

def construire_empreinte(dossier, fichier_empreinte):
    empreinte = {}
    for fichier in dossier.rglob("*"):

        if fichier.is_file():
            
            if fichier == fichier_empreinte:
                continue

            hash_fichier = calculer_hash(fichier)
#Au cas où il y a le meme nom de fichier, on utilise le CHEMIN RELATIF.
# .as_posix() transforme l'objet path en clé lisible par json.
            cle = fichier.relative_to(dossier).as_posix()
            empreinte[cle] = hash_fichier

    return empreinte

def sauvegarder_empreinte(empreinte):
    with fichier_empreinte.open("w", encoding="utf-8") as f_e:
        json.dump(empreinte, f_e, sort_keys=True, indent=4)


def mettre_a_jour_empreinte(empreinte):
    sauvegarder_empreinte(empreinte)


def afficher_rapport(resultats):
    print("=="*20, "RAPPORT", "=="*20)
    print("\nFichiers intacts :")    
    for nom in resultats["ok"]:
        print("-", nom)

    print("\nFichiers modifiés :")
    for fichier in resultats["modifies"]:
        print("-", fichier["nom"])
        print("Ancienne empreinte :", fichier["ancienne"])
        print("Nouvelle empreinte :", fichier["nouvelle"])

    print("\nNouveaux fichiers :")
    for nom in resultats["nouveaux"]:
        print("-", nom)

    print("\nFichiers supprimés :")
    for nom in resultats["supprimes"]:
        print("-", nom)

    print("="*20, "RESUME", "="*20)
    print("Fichiers OK:", len(resultats["ok"]))
    print("Fichiers modifiés:", len(resultats["modifies"]))
    print("Fichiers supprimés:", len(resultats["supprimes"]))
    print("Nouveaux fichiers:", len(resultats["nouveaux"]))

def afficher_menu():
    print("="*15, "MENU", "="*15)
    print("1. Vérifier l'intégrité")      
    print("2. Mettre à jour la référence")
    print("3. Quitter")

    choix = input("Votre choix : ")
    return choix

def charger_empreinte():
# « La référence est-elle structurellement exploitable ? »
    empreinte_valide = True
    empreinte_existe = True
    ancienne_empreinte = {}

    if fichier_empreinte.exists():

        try:
            with fichier_empreinte.open("r", encoding="utf-8") as f_e:
                ancienne_empreinte = json.load(f_e)

            
                if not isinstance(ancienne_empreinte, dict):
                    print("ALERTE : le fichier d'empreintes ne contient pas une structure valide.")
                    empreinte_valide = False

                else:
                    for hash_fichier in ancienne_empreinte.values():

                        if not hash_valide(hash_fichier):
                            empreinte_valide = False
                            break

        except json.JSONDecodeError:
            print("ALERTE : le fichier d'empreintes est invalide.")
            empreinte_valide = False
        
    else:
        print("Première utilisation ! Aucun fichier d'empreintes trouvé.")
        empreinte_valide = False
        empreinte_existe = False
    return ancienne_empreinte, empreinte_existe, empreinte_valide


def hash_valide(hash_fichier):

    if isinstance(hash_fichier, str):
        return len(hash_fichier) == 64 and all(
            caracter in "0123456789abcdef" 
            for caracter in hash_fichier)
    return False



def confirmer_mise_a_jour():
    print("\nVous êtes sur le point de remplacer la référence actuelle.")
    print("Cette action acceptera l'état actuel des fichiers comme nouvelle référence.")

    choix = input("\nConfirmer ? (o/n) :").strip().lower()

    return choix == "o"
  

def main():

    while True:
        choix = afficher_menu()

        if choix == "1":
            print("\nVérification...")    
            ancienne_empreinte, empreinte_existe, empreinte_valide = charger_empreinte()

            if not empreinte_existe:
                empreinte = construire_empreinte(dossier, fichier_empreinte)
                sauvegarder_empreinte(empreinte)
                print("\nLa référence ont été créee.")
            
            elif not empreinte_valide:
                print("Alerte: Le fichier d'empreinte est corrompu ou invalide.")
            
            else:
                empreinte = construire_empreinte(dossier, fichier_empreinte)
                resultats = verifier_integrite(ancienne_empreinte, empreinte)
                afficher_rapport(resultats)





        elif choix == "2":

            ancienne_empreinte, empreinte_existe, empreinte_valide = charger_empreinte()

            if not empreinte_existe:
                print("\nAucune référence existante.")
                print("Utilisez d'abord la vérification pour initialiser le système.")

            elif not empreinte_valide:
                print("MISE A JOUR REFUSE: fichier d'empreinte invalide ou corrompu !")

            else:
                empreinte = construire_empreinte(dossier, fichier_empreinte)

                if confirmer_mise_a_jour():
                    mettre_a_jour_empreinte(empreinte)
                    print("Référence mise à jour avec succès.")  

        elif choix == "3":
            print("Au-revoir.")
            break
        else:
            print("Choix invalide. Veuillez choisir 1, 2 ou 3.")


    if empreinte_valide:
        if not ancienne_empreinte:
            print("="*8, "INITIALISATION", "="*8)
            print("Référence d'intégrité créée.")
            print("Fichiers surveillés:", len(empreinte))
            sauvegarder_empreinte(empreinte)
        else:
            resultats = verifier_integrite(ancienne_empreinte, empreinte)
            afficher_rapport(resultats)        

if __name__ == "__main__":
    main()
