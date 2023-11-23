# Vraag de gebruiker om input
seconden = int(input("Voer het aantal seconden sinds middernacht in: "))

# Berekent de uur-, minuten- en seconden-aanduiding
uren = (seconden // 3600) % 24
minuten = (seconden % 3600) // 60
seconden_restant = seconden % 60

# Druk de resultaten af op één regel gescheiden door dubbelpunten
print(f"{uren}:{minuten}:{seconden_restant}")
