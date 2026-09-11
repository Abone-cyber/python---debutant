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
    try:
        with fichier_empreinte.open("r", encoding="utf-8") as f_e:
            ancienne_empreinte = json.load(f_e)
    except json.JSONDecodeError:
            print("ALERTE : le fichier d'empreintes est invalide.")
            ancienne_empreinte = {}
else:
    ancienne_empreinte = {}
    print("Première utilisation ! Aucun fichier d'empreintes trouvé.")

def verifier_integrite(ancienne_empreinte, empreinte):
    ok = 0
    modifies = 0
    nouveaux = 0
    supprimes = 0

    for nom in ancienne_empreinte:
        if nom in empreinte:
            if ancienne_empreinte[nom] == empreinte[nom]:
                print("Le fichier est OK.")
                ok += 1
            else:
                print(f"ALERTE : {nom} a été modifié !")
                modifies += 1
                print("Ancienne empreinte : ", ancienne_empreinte[nom])
                print("Nouvelle empreinte : ", empreinte[nom])
    for nom in empreinte:
        if nom not in ancienne_empreinte:
            print("Nouveau fichier:", nom)
            nouveaux += 1
                
    for nom in ancienne_empreinte:
        if nom not in empreinte:
            print(f"{nom} a été supprimé.")
            supprimes += 1
    return f"===== RÉSUMÉ =====\n Fichiers OK : {ok}\n Fichiers modifiés: {modifies}\n Nouveaux fichiers: {nouveaux}\n Fichiers supprimés: {supprimes}"


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


empreinte = construire_empreinte(dossier, fichier_empreinte)
sauvegarder_empreinte(empreinte)
verifier_integrite(ancienne_empreinte, empreinte)
























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
