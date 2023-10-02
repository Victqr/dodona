aantal_leerlingen = int(input("Hoeveel leerlingen zijn er? "))
aantal_appels = int(input("Hoeveel appels zijn er? "))
appels_per_leerling = aantal_appels // aantal_leerlingen
overblijvende_appels = aantal_appels % aantal_leerlingen
print(appels_per_leerling)
print(overblijvende_appels)
