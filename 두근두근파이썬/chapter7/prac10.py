import turtle
import random as rd
t = turtle.Turtle()
s = turtle.Screen()
t.width(3)
t.speed(0)
def draw_branch(dis):
    t.pencolor(rd.random(),rd.random(),rd.random())
    for i in range(3):
        t.fd(dis)
        t.rt(45)
        t.fd(dis)
        t.bk(dis)
        t.lt(90)
        t.fd(dis)
        t.bk(dis)
        t.rt(45)
        t.fd(dis)
        t.bk(dis)
    t.bk(dis*3) 


for i in range(8):
    draw_branch(50)
    t.pencolor(rd.random(),rd.random(),rd.random())
    t.lt(360/8)

turtle.done()

