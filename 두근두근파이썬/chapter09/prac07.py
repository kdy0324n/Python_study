import turtle
import random as rd

t = turtle.Turtle()
t.shape("turtle")

colors = ["red","yellow","black","blue","white","orange","green"]


def draw_shape(c,length,sides,x,y):
    t.up()
    t.goto(x,y)
    t.down()
    t.color(c)

    t.begin_fill()
    for i in range(sides):
        t.fd(length)
        t.lt(360/sides)
    t.end_fill()

for i in range(5):
    draw_shape(rd.choice(colors),rd.randint(10,70),rd.randint(3,10),rd.randint(-250,250),rd.randint(-250,250))
turtle.done()
