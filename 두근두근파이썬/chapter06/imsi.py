import turtle
import random as rd

t = turtle.Turtle()


t.shape("turtle")
t.speed(0)


for i in range(30):
    t.up()
    t.goto(rd.randint(-250,250),rd.randint(-250,250))
    t.down()

    t.fillcolor(rd.random(),rd.random(),rd.random())
    width = rd.randint(0,100)
    height = rd.randint(0,100)
    t.begin_fill()
    for i in range(2):
        t.fd(width)
        t.lt(90)
        t.fd(height)
        t.lt(90)
    t.end_fill()
turtle.done()