# De gebruiker wordt gevraagd naar twee gehele getallen in te voeren
a = int(input("Voer de coëfficiënt a in: "))
b = int(input("Voer de constante b in: "))

if a == 0:
    if b == 0:
        print("Er zijn meerdere gehele oplossingen.")
    else:
        print("Er is geen gehele oplossing.")
else:
    x = b // a
    if b % a == 0:
        print(f"De gehele oplossing is x = {x}.")
    else:
        print("Er is geen gehele oplossing.")
