k1 = int(input("Voer het kolomnummer van veld 1 in: "))
r1 = int(input("Voer het rijnummer van veld 1 in: "))
k2 = int(input("Voer het kolomnummer van veld 2 in: "))
r2 = int(input("Voer het rijnummer van veld 2 in: "))

def is_geldige_koningin_zet(k1, r1, k2, r2):
  if k1 == k2 or r1 == r2 or abs(k2 - k1) == abs(r2 - r1):
      return "GELDIGE KONINGIN-ZET"
  else:
      return "ONGELDIGE KONINGIN-ZET"

resultaat = is_geldige_koningin_zet(k1, r1, k2, r2)
print(resultaat)
