def geldige_torensprong(k1, r1, k2, r2):
    return k1 == k2 or r1 == r2

K1 = int(input("Voer het kolomnummer van veld 1 in: "))
R1 = int(input("Voer het rijnummer van veld 1 in: "))
K2 = int(input("Voer het kolomnummer van veld 2 in: "))
R2 = int(input("Voer het rijnummer van veld 2 in: "))

if geldige_torensprong(K1, R1, K2, R2):
    print("GELDIGE TORENZET")
else:
    print("ONGELDIGE TORENZET")
