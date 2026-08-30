class AgeInvalidError(Exception):
    pass

try:
    age = int(input("Entrez votre age : "))
    if age < 0 or age > 120:
        raise AgeInvalidError("Age incorrect.")
except AgeInvalidError as e:
    print(e)
else:
    print("Age accepté.")