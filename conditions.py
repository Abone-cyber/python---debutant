a = int(input("Entrez votre age:"))
if a < 0:
    print("age invalide.")
elif a < 13:
    print("Tu es un enfant.")
elif a >= 13 and a < 18:
    print("Tu es un ado.")
elif a >= 18:
    print("Tu es un adulte.")
