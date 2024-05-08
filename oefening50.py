# Vraag de gebruiker om input
getal = int(input("Voer een natuurlijk getal in (bestaande uit 3 verschillende cijfers): "))

def check_stijgend(getal):
    # Converteer het getal naar een lijst van cijfers
    cijfers = [int(c) for c in str(getal)]
    
    # Controleer of de cijfers in stijgende volgorde staan
    if cijfers == sorted(cijfers):
        return "STIJGEND"
    else:
        return "NIET (!) STIJGEND"

resultaat = check_stijgend(getal)
print(resultaat)

