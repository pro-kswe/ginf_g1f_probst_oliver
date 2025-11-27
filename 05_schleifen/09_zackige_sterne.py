import turtle as t
import random as rd

farbe_1 = "red"
t.pencolor(farbe_1)
t.speed(10)

for _ in range(5):
    a = rd.randrange(50, 201)
    for _ in range(5):
        t.fd(a)
        t.rt(144)
    t.lt(72)
