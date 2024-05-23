# Vraag de gebruiker om een natuurlijk getal N
N = int(input("Voer een natuurlijk getal in: "))

# Initialisatie van het natuurlijk getal en het kwadraat
natuurlijk_getal = 1
kwadraat = 1

# Blijf kwadraten afdrukken totdat kwadraat groter is dan N
while kwadraat <= N:
    print(kwadraat, end=" ")
    natuurlijk_getal += 1
    kwadraat = natuurlijk_getal ** 2
