import PIL.Image as img
import random as rd

bild = img.new("RGB", (5, 10))

r = rd.randrange(0, 256)
g = rd.randrange(0, 256)
b = rd.randrange(0, 256)
farbe = (r, g, b)

# Variante 1
for y in range(0, 10):
    bild.putpixel((2, y), farbe)

# Variante 2
for y in range(0, 10):
    bild.putpixel((2, y), (r, b, g))

bild.save("02_vertikale_linie_ergebnis.png") 
