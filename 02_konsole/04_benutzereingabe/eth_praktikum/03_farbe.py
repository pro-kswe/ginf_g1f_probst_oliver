import random as rd

farbe = input("Wie lautet deine Lieblingsfarbe?")
bewertungen = [f"{farbe} ist echt sehr hübsch", f"{farbe} ist leider völlig out"]
resultat = rd.choice(bewertungen)
print(resultat)
