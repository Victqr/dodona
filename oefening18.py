total_minutes = int(input("Voer de minuten in na middernacht: "))

# Bereken uren en minuten met respect voor dagen
hours = (total_minutes // 60) % 24
minutes = total_minutes % 60

# Create time as a string without leading zeros
time_string = "{} {}".format(hours, minutes)

print(time_string)
