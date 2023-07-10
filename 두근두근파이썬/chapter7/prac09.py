import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('skyblue')
t.fillcolor('white')

def draw_snowman(x,y):
    t.up()
    t.goto(x,y)
    t.down()

    t.begin_fill()
    t.circle(20)
    t.end_fill()

    t.setheading(-90)
    t.up()
    t.bk(10)
    t.down()
    t.setheading(-180)

    t.begin_fill()
    t.circle(15)
    t.end_fill()

    t.setheading(-90)
    t.up()
    t.fd(15)
    t.down()
    t.setheading(-180)

    t.begin_fill()
    t.circle(30)
    t.end_fill()

    t.circle(30,45)
    t.rt(90)
    t.fd(30)
    t.bk(30)
    
    t.rt(90)
    t.circle(-30,90)
    t.lt(90)
    t.fd(30)

    t.setheading(0)

s.onscreenclick(draw_snowman)
turtle.done()
