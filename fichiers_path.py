from pathlib import Path

#Le dossier qui contient le fichier python actuel
dossier_script = Path(__file__).parent

#On assemble deux *chemins*                Ce sont bien des chemins, pas  autres choses.
chemin = dossier_script / "test.txt"

#Va ouvrir le fichier représenté par chemin et lis son contenu sous forme de texte.
contenue = chemin.read_text()
print(contenue)
print(type(contenue))