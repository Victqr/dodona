getal = int(input("Geef een natuurlijk getal: "))

if 100 <= getal <= 999:
    resultaat = "DRIE"
else:
    resultaat = "NIET (!) DRIE"

print(f"{resultaat}")
