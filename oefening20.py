# Vraag de gebruiker om input
decimaal_getal = float(input("Voer een positief decimaal getal in: "))

# Converteer het decimale getal naar een string om het eerste cijfer na het decimale teken te isoleren
decimaal_string = str(decimaal_getal)

# Vind het eerste cijfer na het decimale teken
eerste_cijfer_na_decimaal = int(decimaal_string.split('.')[1][0])

# Druk het geïsoleerde cijfer af
print(f"{eerste_cijfer_na_decimaal}")
