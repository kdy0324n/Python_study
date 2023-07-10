import turtle
import random as rd

t = turtle.Turtle()
s = turtle.Screen()

def draw_house(x,y):
    t.up()
    t.goto(x,y)
    t.down()

    t.fillcolor(rd.random(),rd.random(),rd.random())
    t.begin_fill()
    for i in range(3):
        t.fd(60)
        t.lt(120)
    for i in range(4):
        t.fd(60)
        t.rt(90)
    t.end_fill()

s.onscreenclick(draw_house)
turtle.done()
    
    