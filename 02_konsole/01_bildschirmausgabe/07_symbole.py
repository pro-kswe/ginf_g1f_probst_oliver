import random as rd

symbole = ["*", "$", "€", ":-)", ":-("]
symbol = rd.choice(symbole)
for _ in range(4):
  print(4 * symbol)
