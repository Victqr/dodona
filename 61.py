maand = int(input("Voer een getal tussen 1 en 12 in om de dagen in die maand te weten: "))

if not 1 <= maand <= 12:
    print("Ongeldige invoer. Voer een getal tussen 1 en 12 in.")
else:
    if maand in [4, 6, 9, 11]:
        dagen = 30
    elif maand == 2:
        dagen = 28
    else:
        dagen = 31

    print(dagen)
