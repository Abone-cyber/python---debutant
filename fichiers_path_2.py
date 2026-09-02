from pathlib import Path

dossier_acctuel = Path(__file__).parent
chemin = dossier_acctuel / "test.txt"

chemin.write_text("Python\nCybersécurité\nModules", encoding="utf-8")
contenue = chemin.read_text(encoding="utf-8")
print(contenue)