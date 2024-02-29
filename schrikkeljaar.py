def is_schrikkeljaar(jaar):
  if (jaar % 4 == 0 and jaar % 100 != 0) or (jaar % 400 == 0):
      return "SCHRIKKELJAAR"
  else:
      return "GEEN SCHRIKKELJAAR"
jaar = int(input("Voer een jaartal in: "))
resultaat = is_schrikkeljaar(jaar)
print(resultaat)
