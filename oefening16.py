def bereken_wijzer_positie(uren, minuten):
    # Converteer uren naar het juiste formaat (12-uurs klok)
    uren = uren % 12

    # Bereken de positie van de wijzer in graden
    positie = int((uren * 60 + minuten) * 0.5)

    return positie

# Vraag de gebruiker om input
uren = int(input("Voer het aantal uren in (0-23): "))
minuten = int(input("Voer het aantal minuten in (0-59, even getal): "))

# Controleer of minuten even zijn
if minuten % 2 != 0:
    print("Ongeldige invoer voor minuten. Moet een even getal zijn.")
else:
    # Bereken en druk de positie van de wijzer af
    positie = bereken_wijzer_positie(uren, minuten)
    print(f"{positie}")
