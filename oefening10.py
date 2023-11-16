Getal=int(input("Geef een getal in groter of gelijk aan 100."))

Getal_zondertiental=Getal//100
Tiental=Getal%100

Getal_1=Tiental//10
Getal_1=str(Getal_1)

Getal_2=Tiental%10
Getal_2=str(Getal_2)

Getal_zondertiental=str(Getal_zondertiental)

print(Getal_zondertiental+Getal_2+Getal_1)
