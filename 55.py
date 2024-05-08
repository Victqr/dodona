maand = int(input("Voer de maand in (1-12): "))
dag = int(input("Voer de dag in (1-31): "))

if not 1 <= maand <= 12:
    print("Ongeldige maand. De maand moet tussen 1 en 12 liggen.")
    exit()
if not 1 <= dag <= 31:
    print("Ongeldige dag. De dag moet tussen 1 en 31 liggen.")
    exit()

maand_lengte = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

volgende_dag = dag + 1
if volgende_dag > maand_lengte[maand - 1]:
    volgende_dag = 1
    volgende_maand = maand + 1
else:
    volgende_maand = maand

if maand == 2 and dag == 29:
    volgende_dag = 1
    volgende_maand = maand + 1

if volgende_maand > 12:
    volgende_maand = 1

print(volgende_maand)
print(volgende_dag)
