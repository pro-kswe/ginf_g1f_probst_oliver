import turtle
import random

farbe_1 = "red"
farbe_2 = "green"
farbe_3 = "blue"
staerke = random.randrange(1, 6)
d = random.randrange(5, 26)
x_1 = random.randrange(-100, 101)
x_2 = random.randrange(-100, 101)
x_3 = random.randrange(-100, 101)
y_1 = random.randrange(-200, 201)
y_2 = random.randrange(-200, 201)
y_3 = random.randrange(-200, 201)
turtle.pensize(staerke)
turtle.pu()
turtle.goto(x_1, y_1)
turtle.pd()
turtle.pencolor(farbe_1)
turtle.dot(d)
turtle.goto(x_2, y_2)
turtle.pencolor(farbe_2)
turtle.dot(d)
turtle.goto(x_3, y_3)
turtle.pencolor(farbe_3)
turtle.dot(d)
turtle.goto(x_1, y_1)
