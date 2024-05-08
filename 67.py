# Vraag de gebruiker om drie gehele getallen in te voeren
getal1 = int(input("Voer het eerste gehele getal in: "))
getal2 = int(input("Voer het tweede gehele getal in: "))
getal3 = int(input("Voer het derde gehele getal in: "))

# Controleer hoeveel gelijke getallen er zijn
if getal1 == getal2 == getal3:
    print(3)
elif getal1 == getal2 or getal1 == getal3 or getal2 == getal3:
    print(2)
else:
    print(0)
