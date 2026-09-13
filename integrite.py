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
#Au cas où il y a le meme nom de fichier dans les sous_dossiers de dosssier, on utilise le CHEMIN RELATIF.
# .as_posix() transforme l'objet path en clé lisible par json.
            cle = fichier.relative_to(dossier).as_posix()
            empreinte[cle] = hash_fichier

    return empreinte

def sauvegarder_empreinte(empreinte):
    with fichier_empreinte.open("w", encoding="utf-8") as f_e:
        json.dump(empreinte, f_e, sort_keys= True, indent=4)


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

        

def main():
    empreinte = construire_empreinte(dossier, fichier_empreinte)

    empreinte_valide = True
    if fichier_empreinte.exists():
        try:
            with fichier_empreinte.open("r", encoding="utf-8") as f_e:
                ancienne_empreinte = json.load(f_e)
        except json.JSONDecodeError:
            print("ALERTE : le fichier d'empreintes est invalide.")
            ancienne_empreinte = {}
            empreinte_valide = False
    else:
        print("Première utilisation ! Aucun fichier d'empreintes trouvé.")
        ancienne_empreinte = {}

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
