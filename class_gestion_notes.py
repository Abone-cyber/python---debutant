from class_eleve import Eleve

class GestionNotes:
    def __init__(self):
        self.eleves = []

    def ajouter_eleve(self):
        nom = input("Nom de l'élève :").lower()
        self.eleves.append(Eleve(nom))
        print("\nElève enregistré(e)")
        self.sauvegarder()
        

    def afficher_eleves(self):
        if not self.eleves:
            print("la liste est vide.")
        else:
            for eleve in self.eleves:
                print(eleve)
        

    def rechercher_eleve(self):
        nom = input("Nom de l'élève : ")
        trouve = False
        for eleve in self.eleves:
            if nom.lower() in eleve.nom.lower():
                eleve.afficher()
                trouve = True
                break
        if not trouve:
            print("Cet élève n'est pas enregisté.")


    def supprimer_eleve(self):
        nom = input("Nom de l'élève : ")
        for eleve in self.eleves:
            if eleve.nom.lower() == nom.lower():
                self.eleves.remove(nom)
                print(f"Elève {nom} supprimé.")
                return
        print("Elève non trouvé.")
        self.sauvegarder()

    
    def modifier_notes(self):
        noms = input("Nom de l'élève : ")
        for eleve in self.eleves:
            if noms.lower() not in eleve.nom.lower():
                print("Cet élève n'est pas enregistré.")
                return
        else:
            try:
                nouvelle_note = float(input("Nouvelle note : "))
                eleve.notes = nouvelle_note
            except ValueError:
                print("Erreur : entrez une note valide.")
        self.sauvegarder()

    def ajouter_notes(self):
        nom = input("Nom : ")
        for eleve in self.eleves:
            if eleve.nom.lower() == nom.lower():
                n_note = float(input("Note à ajouter : "))
                eleve.ajouter_note(n_note)
            else:
                print("Cet élève n'est pas enegistré(e). Veuillez le faire\n")
                self.ajouter_eleve()
        self.sauvegarder()

    
    def sauvegarder(self, nom_fichier):
        try:
            with open(nom_fichier, "w", encoding="utf-8") as f:
                for eleve in self.eleves:
                    notes_str = ", ".join(str(note) for note in eleve.notes) 
                    f.write(f"{eleve.nom} : {notes_str}")
                    print("Données sauvegardées avec succès.")       
        except Exception as e:
            print("Erreur lors de la sauvegarde : ", e)


def menu ():
    gestion = GestionNotes()
    while True:
        print("\n--- MENU ---")
        print("1. Ajouter un élève ")
        print("2. Afficher tout les élèves")
        print("3. Rechercher un élève")
        print("4. Supprimer un élève")
        print("5. Modifier les notes d'un élève")
        print("6. Ajouter une note ")
        print("7. Quitter")

        choix = input("\nVotre choix : ")
        
        if choix == "1":
           gestion.ajouter_eleve()
        elif choix =="2":
            gestion.afficher_eleves()
        elif choix == "3":
            gestion.rechercher_eleve()
        elif choix == "4":
            gestion.supprimer_eleve()
        elif choix == "5":
            gestion.modifier_notes()            
        elif choix == "6":
             gestion.ajouter_notes()
        elif choix == "7":
            print("Au-revoir !")
            break
           
        else:
            print("Option invalide. Veuillez réessayer.")
menu()
        