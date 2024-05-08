k1 = int(input("Voer het kolomnummer van veld 1 in: "))
r1 = int(input("Voer het rijnummer van veld 1 in: "))
k2 = int(input("Voer het kolomnummer van veld 2 in: "))
r2 = int(input("Voer het rijnummer van veld 2 in: "))

def geldige_zet(k1, r1, k2, r2):
    horizontale_afstand = abs(k2 - k1)
    verticale_afstand = abs(r2 - r1)
    if (horizontale_afstand == 2 and verticale_afstand == 1) or (horizontale_afstand == 1 and verticale_afstand == 2):
        return "GELDIGE ZET"
    else:
        return "ONGELDIGE ZET"

resultaat = geldige_zet(k1, r1, k2, r2)
print(resultaat)
