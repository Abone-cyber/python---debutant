from pathlib import Path
import hashlib
import json
dossier = Path(__file__).parent


fichier_empreinte = dossier / "empreintes.json"



def calculer_hash(fichier):
    contenu = fichier.read_bytes()
    hash_obj = hashlib.sha256(contenu)
    return hash_obj.hexdigest()


if fichier_empreinte.exists():
    with fichier_empreinte.open("r", encoding="utf-8") as f_e:
        ancienne_empreinte = json.load(f_e)
        if not ancienne_empreinte:
            print ("Première utilisation ! empreinte.json est vide.")
else:
    ancienne_empreinte = {}
    print("Première utilisation ! empreinte.json est vide.")

def verifier_integrite(ancienne_empreinte, empreinte):

    for nom in ancienne_empreinte:
        if nom in empreinte:
            if ancienne_empreinte[nom] == empreinte[nom]:
                print("Le fichier est OK.")
            else:
                print(f"ALERTE : {nom} a été modifié !")
             
    for nom in empreinte:
        if nom not in ancienne_empreinte:
            print("Nouveau fichier:", nom)
                
    for nom in ancienne_empreinte:
        if nom not in empreinte:
            print(f"{nom} a été supprimé.")
            

        

def construire_empreinte(dossier, fichier_empreinte):
    empreinte = {}
    for fichier in dossier.rglob("*"):

        if fichier.is_file():
            
            if fichier == fichier_empreinte:
                continue

            hash_fichier = calculer_hash(fichier)
            empreinte[fichier.name] = hash_fichier

    return empreinte

def sauvegarder_empreinte(empreinte):
        with fichier_empreinte.open("w", encoding="utf-8") as f_e:
            json.dump(empreinte, f_e, sort_keys= True, indent=4)

if not ancienne_empreinte:
    sauvegarder_empreinte(empreinte)


def mettre_a_jour_empreinte(empreinte):
    sauvegarder_empreinte(empreinte)



    # Empreinte{} contient les hash qui sont calculés pour véfirier l'intégrité des fichiers (leur état actuel)
    # ancienne_empreinte{} contient les hashs des fichiers dans leur état <<initiale>>, <<intègre>>

#ancienne empreinte        état actuel
#       ↓                       ↓
#    JSON                    fichiers
#
#       └──── comparaison ──────┘
#                 ↓
#      ┌──────────┼──────────┐
#      ↓          ↓          ↓
#   OK        MODIFIÉ      NOUVEAU
#                            +
#                         SUPPRIMÉ
