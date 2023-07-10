import random as rd
import turtle
t = turtle.Turtle()

C = ["red","blue","brown","green","orange","purple"]

t.speed(0)

for i in range(30):
    t.fillcolor(rd.choice(C))
    x = rd.randrange(-250,250)
    y = rd.randrange(-250,250)
    length = rd.randrange(1,30)

    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.circle(length)
    t.end_fill()
t.done()