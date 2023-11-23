# Vraag gebruiker om het gehele deel van de prijs van 1 koekje
g = int(input("Geef het gehele deel van de prijs van 1 koekje: "))

# Vraag gebruiker om het decimale deel van de prijs van 1 koekje
d = int(input("Geef het decimale deel van de prijs van 1 koekje (0 <= d < 100): "))

# Vraag gebruiker om het aantal koekjes
n = int(input("Geef het aantal koekjes: "))

# Bereken totaal bedrag
totaal_bedrag = (g + d/100) * n

# Haal het gehele deel uit totaal_bedrag
euro_deel = int(totaal_bedrag)

# Haal het decimale deel uit totaal_bedrag en vermenigvuldig met 100 om het in eurocenten te krijgen
cent_deel = round((totaal_bedrag - euro_deel) * 100)

# Aanpassing om afrondingsfouten te voorkomen
if cent_deel == 100:
    euro_deel += 1
    cent_deel = 0

# Toon resultaat
print(f"{euro_deel} {cent_deel}")
