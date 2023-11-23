# Vraag de gebruiker om input
getal = int(input("Voer een getal in van 2 cijfers (10-99): "))

# Controleer of het ingevoerde getal voldoet aan de voorwaarde
if 10 <= getal < 100:
    # Isoleer het tiental en de eenheid
    tiental = getal // 10
    eenheid = getal % 10

    # Druk beide cijfers af, gescheiden door een spatie
    print(tiental, eenheid)
else:
    print("Ongeldige invoer. Voer een getal in van 2 cijfers.")
