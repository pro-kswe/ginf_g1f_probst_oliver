import turtle

farbe_1 = "red"  # "red" ist ein String (umgangsprachlich Text)
farbe_2 = "green"
farbe_3 = "blue"
staerke = 3  # 3 ist ein Int (kurz für Integer (deutsch: ganze Zahl))
d = 10
turtle.pensize(staerke)
turtle.pu()
turtle.goto(50, 0)
turtle.pd()
turtle.pencolor(farbe_1)
turtle.dot(d)
turtle.goto(150, 0)
turtle.pencolor(farbe_2)
turtle.dot(d)
turtle.goto(75, 200)
turtle.pencolor(farbe_3)
turtle.dot(d)
turtle.goto(50, 0)
