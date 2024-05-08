k1 = int(input("Voer het kolomnummer van veld 1 in: "))
r1 = int(input("Voer het rijnummer van veld 1 in: "))
k2 = int(input("Voer het kolomnummer van veld 2 in: "))
r2 = int(input("Voer het rijnummer van veld 2 in: "))

def is_geldige_koningzet(k1, r1, k2, r2):
  if abs(k2 - k1) <= 1 and abs(r2 - r1) <= 1:
      return "GELDIGE KONINGZET"
  else:
      return "ONGELDIGE KONINGZET"

resultaat = is_geldige_koningzet(k1, r1, k2, r2)
print(resultaat)
