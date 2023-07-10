import turtle 
import random as rd
t = turtle.Turtle()

C = ["red","blue","brown","green","orange","purple"]


for i in range(30):
    t.color(rd.choice(C))
    x = rd.randrange(-250,250)
    y = rd.randrange(-250,250)
    length = rd.randrange(1,100)


    t.up()
    t.goto(x,y)
    t.down()

    t.begin_fill()
    for j in range(5):
        t.fd(length)
        t.rt(144)
    t.end_fill()
turtle.done()