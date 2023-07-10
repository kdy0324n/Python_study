import turtle
import random as rd

t = turtle.Turtle()

color = ["red","blue","yellow"]

def draw_square(x,y,c):
    t.up()
    t.goto(x,y)
    t.down()
    t.fillcolor(c)

    t.begin_fill()
    for i in range(4):
        t.fd(100)
        t.rt(90)
    t.end_fill()
    
for i in color:
    draw_square(rd.randrange(-250,250),rd.randrange(-250,250),i)
