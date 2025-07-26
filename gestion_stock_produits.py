stock ={}

def ajouter_produit():
    print("\nAjout d'un produit.")
    nom = input("Nom du produit : ").lower()
    if nom in stock:
        print("Ce produit existe déjà.")
        return
    try:
        quantite = int(input("Quantité : "))
        prix = int(input("Prix : "))
        stock[nom] = {"quantité": quantite, "prix": prix}
        print(f"{nom} ajouté avec succès.")
    except ValueError:
        print("Erreur : Veuillez entrer des nombres pour la quantité et le prix.")

def afficher_stock():
    if not stock:
        print("Le stock est vide.")
    else:
        print("\n--- Stock actuel ---")
    for nom, infos in stock.items():
        print(f"Produit : {nom} | Quantité : {infos["quantité"]} | Prix : {infos["prix"]} FCFA")
        print("-" * 50)

def rechercher_produit():
    print("\nVous rechercher un produit.")
    nom = input("Nom du produit : ").lower()
    if nom in stock:
        infos = stock[nom]
        print(f"Nom : {nom} | Quantité : { infos["quantité"]} | Prix : {infos["prix"]}")
    else:
        print("Ce produit n'est pas disponible.")

def supprimer_produit():
    print("\n Vous voulez supprimer un produit.")
    nom = input("Nom du produit : ").lower()
    if nom in stock:
        del stock[nom]
        print(f"Le produit : {nom}, a bien été supprimé.") 

def modifier_quantite():
    print("\n Vous voulez modifier une quantité")
    nom = input("Nom du produit : ").lower()
    if nom in stock:
        try:
            nouvelle_quantité = int(input("Entrez la nouvelle quantité pour ce produit : "))
            stock[nom]["quantité"] = nouvelle_quantité
            print(f"Quantité de {nom} mis à jour.")
        except ValueError:
            print("Erreur : entrez un nombre entier.")
    else:
        print("Ce produit n'est pas disponible.")

def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Ajouter un produit")
        print("2. Afficher le stock")
        print("3. Rechercher un produit")
        print("4. Supprimer un produit")
        print("5. Modifier la quantité")
        print("6. Quitter")

        choix = input("\nVotre choix : ")

        if choix == "1":
            ajouter_produit()
        elif choix == "2":
            afficher_stock()
        elif choix == "3":
            rechercher_produit()        
        elif choix == "4":
            supprimer_produit()
        elif choix == "5":
            modifier_quantite()
        elif choix =="6":
            print("Au-revoir !")
            break
        else:
            print("Option invalide. Veuillez recommencer.")
menu()