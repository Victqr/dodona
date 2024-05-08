getal1 = int(input("Voer het eerste getal in: "))
getal2 = int(input("Voer het tweede getal in: "))
getal3 = int(input("Voer het derde getal in: "))

if getal1 == getal2 or getal1 == getal3 or getal2 == getal3:
    if getal1 != getal2 and getal1 != getal3:
        print("Het eerste getal, nl. " + str(getal1) + " is het zwarte schaap.")
    elif getal2 != getal1 and getal2 != getal3:
        print("Het tweede getal, nl. " + str(getal2) + " is het zwarte schaap.")
    else:
        print("Het derde getal, nl. " + str(getal3) + " is het zwarte schaap.")
else:
    print("De ingevoerde getallen zijn ongeldig. Er moeten 2 getallen aan elkaar gelijk zijn.")
