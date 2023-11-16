# Vraag de gebruiker naar de hoek van de kleine wijzer
hoek_kleine_wijzer = int(input("Hoek van de kleine wijzer (in graden): "))

# Bereken de positie van de grote wijzer
positie_grote_wijzer = (hoek_kleine_wijzer % 30) * 12

# Druk het resultaat af
print(positie_grote_wijzer)
