a_number = int(input("Geef CIJFERPALINDROOM op: "))

def palindrome(number):
    number = str(number)
    return number == number[::-1]

if palindrome(a_number):
    print("EEN CIJFERPALINDROOM")
else:
    print("GEEN CIJFERPALINDROOM")
