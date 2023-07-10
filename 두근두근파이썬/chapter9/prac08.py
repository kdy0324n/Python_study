import turtle 
import random as rd

t = turtle.Turtle()
t.speed(0)
def draw_star(color,length,x,y):
    t.up()
    t.goto(x,y)
    t.down()
    t.color(color)

    t.begin_fill()
    for i in range(5):
        t.fd(length)
        t.rt(144)
    t.end_fill()

color = ["red","orange","green","brown","blue","skyblue","yellow"]

for i in range(30):
    draw_star(color[rd.randint(0,len(color)-1)],rd.randint(10,60),rd.randint(-250,250),rd.randint(-250,250))
turtle.done()
    
