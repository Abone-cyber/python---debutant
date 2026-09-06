from pathlib import Path
import hashlib
import json
dossier = Path(__file__).parent

nombre_total = 0
nombre_python = 0
nombre_texte = 0
nombre_autres = 0
taille_totale = 0
empreinte = {}
fichier_empreinte = dossier / "empreintes.json"



def calculer_hash(fichier):
    contenu = fichier.read_bytes()
    hash_obj = hashlib.sha256(contenu)
    return hash_obj.hexdigest()

for fichier in dossier.rglob("*"):

    if fichier.is_file():
        taille = fichier.stat().st_size
        nombre_total += 1
        taille_totale += taille

        if fichier.suffix == ".py":
            nombre_python += 1
        elif fichier.suffix == ".txt":
            nombre_texte += 1
        else:
            nombre_autres += 1

        if taille > 800:
            print(fichier.name, "→", taille, "octets")

        if fichier == fichier_empreinte:
            continue
        hash_fichier = calculer_hash(fichier)
        empreinte[fichier.name] = hash_fichier


with fichier_empreinte.open("w", encoding="utf-8") as f_e:
    json.dump(empreinte, f_e, sort_keys= True, indent=4)


if fichier_empreinte.exists():
    with fichier_empreinte.open("r", encoding="utf-8") as f_e:
        ancienne_empreinte = json.load(f_e)
else:
    ancienne_empreinte = {}
    print("Première utilisation ! empreinte.json est vide.")

for fichier in dossier.rglob("*"):
    if fichier.is_file():
        if fichier.name in ancienne_empreinte:
            ancien_hash = ancienne_empreinte[fichier.name]

        if ancien_hash == hash_fichier:
            print("Le fichier est OK.")
        else:
            print(f"ALERTE : {fichier.name} a été modifié !")







#print("=== ANALYSE DU DOSSIER ===")
#print("Fichiers trouvés : ", nombre_total)
#print("Fichiers Python : ", nombre_python)
#print("Fichiers texte : ", nombre_texte)
#print("Autres fichiers  : ", nombre_autres)
#print(f"Taille totale : {taille_totale} octets")
