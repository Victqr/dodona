
k1 = int(input("Voer het kolomnummer van veld 1 in: "))
r1 = int(input("Voer het rijnummer van veld 1 in: "))
k2 = int(input("Voer het kolomnummer van veld 2 in: "))
r2 = int(input("Voer het rijnummer van veld 2 in: "))

def is_geldige_loperzet(k1, r1, k2, r2):
  if abs(k2 - k1) == abs(r2 - r1):
      return "GELDIGE LOPERZET"
  else:
      return "ONGELDIGE LOPERZET"

resultaat = is_geldige_loperzet(k1, r1, k2, r2)
print(resultaat)
