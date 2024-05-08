g1 = int(input("Voer het eerste gehele getal in: "))
g2 = int(input("Voer het tweede gehele getal in: "))

positief_g1 = g1 > 0
positief_g2 = g2 > 0

if (positief_g1 and not positief_g2) or (positief_g2 and not positief_g1):
    print("EXACT 1 POSITIEF")
else:
    print("NIET VOLDAAN")
