getal = int(input("Voer een natuurlijk getal in (kleiner dan 1000): "))
eenheid = getal % 10
tiental = (getal // 10) % 10
honderdtal = getal // 100
som = eenheid + tiental + honderdtal
print(som)
