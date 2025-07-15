notes = [12, 15, 9, 18, 14]
for n in notes:
    print(n)

print("\nLa moyenne de ces notes est de : ")
moyenne = sum(notes) / len(notes)
print(moyenne)

prenoms = ["Nelson", "Mandela", "Junior"]
matieres = ["math", "physique", "chimie"]
for p in prenoms:
    for m in matieres:
        print(p, m)
