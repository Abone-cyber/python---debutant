print("Boucle for :")
for i in range(2, 21, 2):
    print(i)

    print("\nBoucle while :")
    i = 2
    while i <= 20:
        print(i)
        i += 2
        mot = input("\nEntrez un mot :" )
        for lettre in mot:
            print(lettre)
