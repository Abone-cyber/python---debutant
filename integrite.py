from pathlib import Path
import hashlib

dossier = Path(__file__).parent
fichier = dossier / "test.txt"

def calculer_hash(fichier):
    contenu = fichier.read_bytes()
    empreinte = hashlib.sha256(contenu)
    return empreinte.hexdigest()

fichier_hash = dossier / "empreinte.txt"

nouveau_hash = calculer_hash(fichier)

if fichier_hash.exists():
    ancien_hash = fichier_hash.read_text(encoding="utf-8")
else:
    fichier_hash.write_text(nouveau_hash, encoding = "utf-8")
    ancien_hash = nouveau_hash

if ancien_hash == nouveau_hash:
    print("Intégrité OK : le fichier n'a pas changé.")
else:
    print("ALERTE : le fichier a été modifié !")