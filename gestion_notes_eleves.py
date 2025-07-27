notes = {}

def ajouter_eleve():
    nom = input("Nom de l'elève : ").lower()
    if nom in notes:
        print("Cet élève est déjà enregistré.")
        return
    else:
        notes[nom] = []
        print(f"{nom} a été ajouter à la liste.")

def ajouter_note():
    nom  = input("Nom de l'élève : ").lower()
    if nom in notes:
        try:
            note = float(input("Note :"))
            notes[nom].append(note)
            print("Note ajouté !")
        except ValueError:
            print("Veuillez entrer une valeur numérique.")
    else:
        print("Elève introuvable")

def afficher_notes():
    nom  = input("Nom de l'élève : ").lower()
    if  nom in notes:
       print(f"Notes de {nom} : {notes[nom]}")
    else:
        print("Elève introuvable")
    
    
def calcul_moyenne_eleve():
    nom  = input("Nom de l'élève : ").lower()
    if  nom in notes and notes[nom]:
        moyenne = sum(notes[nom]) / len(notes[nom])
        print(f"{nom} a une moyenne de  {moyenne: .2f}")
    elif nom in notes:
        print("Aucune note ergistrée pour cet élève.")
    else:
        print("Elève introuvable.")

def supprimer_élève():
    nom  = input("Nom de l'élève : ").lower()
    if nom in notes:
        del notes[nom]
        print(f"{nom} supprimé(e) de la liste.")
    else:
        print("Elève introuvable.")

def afficher_tout_les_eleves_avec_leur_notes():
    print("Liste des élèves et de leur note : ")
    for nom in notes:
        print(f"{nom} : {notes[nom]}")

def menu():
    while True:
        print("==== MENU ====")
        print("1. Ajouter un élève")
        print("2. Ajouter une note")
        print("3. Afficher les notes d'un élève" )
        print("4. Afficher la moyenne d'un élève")
        print("5. Afficher la liste des élèves et de leurs notes")
        print("6. Quitter le programme")

        choix = input("Votre choix : ")
        if choix == "1":
            ajouter_eleve()
        elif choix == "2":
            ajouter_note()
        elif choix == "3":
            afficher_notes()
        elif choix =="4":
            calcul_moyenne_eleve()
        elif choix == "5":
            afficher_tout_les_eleves_avec_leur_notes()
        elif choix == "6":
            print("Au-revoir !")
            break
        else:
            print("Option invalide veuillez recommencer.")
menu()