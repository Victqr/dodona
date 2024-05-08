x1 = int(input("Voer de x-coördinaat van het eerste hoekpunt in: "))
y1 = int(input("Voer de y-coördinaat van het eerste hoekpunt in: "))
x2 = int(input("Voer de x-coördinaat van het tweede hoekpunt in: "))
y2 = int(input("Voer de y-coördinaat van het tweede hoekpunt in: "))
x3 = int(input("Voer de x-coördinaat van het derde hoekpunt in: "))
y3 = int(input("Voer de y-coördinaat van het derde hoekpunt in: "))

if x1 == x2:
    x4 = x3
elif x1 == x3:
    x4 = x2
else:
    x4 = x1

if y1 == y2:
    y4 = y3
elif y1 == y3:
    y4 = y2
else:
    y4 = y1

print(x4)
print(y4)
