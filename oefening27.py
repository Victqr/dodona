getal = int(input("Voer een natuurlijk getal in (bestaande uit 3 verschillende cijfers): "))

def check_stijgend(getal):
    cijfers = [int(c) for c in str(getal)]
    
    if cijfers == sorted(cijfers):
        return "STIJGEND"
    else:
        return "NIET (!) STIJGEND"

resultaat = check_stijgend(getal)
print(resultaat)

