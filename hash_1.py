from pathlib import Path
import hashlib
dossier = Path(__file__).parent

nombre_total = 0
nombre_python = 0
nombre_texte = 0
nombre_autres = 0
taille_totale = 0
liste_nom =[]
liste_hash = []

def calculer_hash(fichier):
    contenu = fichier.read_bytes()
    empreinte = hashlib.sha256(contenu)
    return empreinte.hexdigest()

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

        if taille > 300:
            print(fichier.name, "→", taille, "octets")

        hash_fichier= calculer_hash(fichier)
        liste_nom.append(fichier.name)
        liste_hash.append(hash_fichier)

print("=== ANALYSE DU DOSSIER ===")
print("Fichiers trouvés : ", nombre_total)
print("Fichiers Python : ", nombre_python)
print("Fichiers texte : ", nombre_texte)
print("Autres fichiers  : ", nombre_autres)
print(f"Taille totale : {taille_totale} octets")
for nom, hash_f in zip(liste_nom, liste_hash):
    print(nom, "--->", hash_f)