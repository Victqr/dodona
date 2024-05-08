# Vraag de gebruiker om vijf gehele getallen in te voeren
getal1 = int(input("Voer het eerste gehele getal in: "))
kleinste_getal = getal1

# Vraag de gebruiker om de resterende vier getallen in te voeren en vind het kleinste getal
for i in range(2, 6):
    getal = int(input(f"Voer het {i}e gehele getal in: "))
    if getal < kleinste_getal:
        kleinste_getal = getal

# Druk het kleinste getal af
print(kleinste_getal)
