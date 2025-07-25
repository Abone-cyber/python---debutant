contacts = {"Alice": "694123456", "Bob": "678912345", "Diane": "652789123"}
def Ajouter_contact(nom, contact):
    contacts[nom] = contact
    print("Contact enregistré.")

def supprimer_contact(nom):
    if nom in contacts:
        del contacts[nom]
        print(f"Contact, {contacts[nom]}  a été supprimé avec succès.")
    else:
        print("Ce contact est introuvable.")

def modifier_numero(nom, nouveau_numero):
    if nom in contacts:
        contacts[nom] = nouveau_numero
        print("Numéro modifié avec succès.")
    else:
        print("Contact introuvable.")

def rechercher_contact(nom):
    if nom in contacts:
        print(f"{nom} : {contacts[nom]}")
    else:
        print("Contact introuvable.")

def afficher_contact():
    for nom, contact in contacts.items():
        print(f"{nom} : {contact}")
    
def menu():
    while True:
        print("\n", "-" * 30)
        print("1. Ajouter un contact")
        print("2. Supprimer un contact")
        print("3. Modifier un numéro")
        print("4. Rechercer un contact")
        print("5. Afficher tous les contacts")
        print("6. Quitter")
        
        choix = input("Votre choix : ")

        if choix == "1":
            print("\nVous voulez ajouter un contact.")
            nom = input("Entrez le nom : ")
            numero = int(input("Numéro : "))
            Ajouter_contact(nom, numero)
        elif choix == "2":
            print("\nVous voulez supprimer un contact")
            nom = input("Le nom du contact à supprimé : ")
            supprimer_contact(nom)
        elif choix == "3":
            print("\nVous voulez modifier un numéro.")
            nom = input("Le nom du contact : ")
            nouveau_numero = int(input("Nouveau numéro : "))
            modifier_numero(nom, nouveau_numero)
        elif choix == "4":
            print("Vous rechercher un contact.")
            nom = input("Le nom du contact : ")
            rechercher_contact(nom)
        elif choix == "5":
            print("\n Liste des cintacts : ")
            afficher_contact()
        elif choix == "6":
            print("Au revoir !")
            break
        else:
            print("Option invalide.")
menu()
