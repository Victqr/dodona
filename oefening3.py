u1 = int(input("Voer het aantal uren in voor het eerste tijdstip: "))
m1 = int(input("Voer het aantal minuten in voor het eerste tijdstip: "))
s1 = int(input("Voer het aantal seconden in voor het eerste tijdstip: "))

u2 = int(input("Voer het aantal uren in voor het tweede tijdstip: "))
m2 = int(input("Voer het aantal minuten in voor het tweede tijdstip: "))
s2 = int(input("Voer het aantal seconden in voor het tweede tijdstip: "))

tijdverschil = (u2 - u1) * 3600 + (m2 - m1) * 60 + (s2 - s1)

print(f"{tijdverschil}")
