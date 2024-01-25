h1 = int (input()) 
w1 = int (input()) 
h2 = int (input()) 
w2 = int (input()) 

if ((h1 % 2 != 0) and (w1 % 2 != 0)) or ((h1 % 2 == 0) and (w1 % 2 == 0)):
    one = str ('black')
else:
    one = str ('white')

if ((h2 % 2 != 0) and (w2 % 2 != 0)) or ((h2 % 2 == 0) and (w2 % 2 == 0)):
    two = str ('black')
else:
    two = str ('white')

#compare two cells
if one == two:
    print ('DEZELFDE KLEUR')
else:
    print ('VERSCHILLENDE KLEUR')
