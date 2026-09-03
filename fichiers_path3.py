from pathlib import Path

dossier = Path(__file__).parent

nombre_total = 0
nombre_python = 0
nombre_texte = 0
nombre_autres = 0
taille_totale = 0

for fichier in dossier.rglob("*"):
    taille = fichier.stat().st_size

    if fichier.is_file():
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

print("=== ANALYSE DU DOSSIER ===")
print("Fichiers trouvés : ", nombre_total)
print("Fichiers Python : ", nombre_python)
print("Fichiers texte : ", nombre_texte)
print("Autres fichiers  : ", nombre_autres)
print(f"Taille totale : {taille_totale} octets")