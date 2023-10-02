getal = int(input("Voer een natuurlijk getal (groter dan of gelijk aan 10) in: "))
if getal >= 10:
    laatste_twee_cijfers = getal % 100
    print(laatste_twee_cijfers)
else:
    print("Het ingevoerde getal moet groter zijn dan of gelijk aan 10.")
