import turtle

t = turtle.Turtle()
t.shape('turtle')
def blue_square():
    t.up()
    t.color('blue')
    t.goto(-150,0)
    t.down()
    t.begin_fill()
    t.forward(300)
    t.lt(90)
    t.forward(80)
    t.lt(90)
    t.fd(300)
    t.lt(90)
    t.fd(80)
    t.end_fill()

def brown_square():
    t.up()
    t.color('brown')
    t.goto(-40,80)
    t.setheading(0)
    t.down()

    t.begin_fill()
    t.fd(80)
    t.lt(90)
    t.fd(40)
    t.lt(90)
    t.fd(80)
    t.lt(90)
    t.fd(40)
    t.end_fill()

def black_wheel():
    t.up()
    t.color('black')
    t.goto(-100,-30)
    t.setheading(0)
    t.down()

    t.begin_fill()
    t.circle(30)
    t.end_fill()

    t.up()
    t.goto(100,-30)
    t.down()

    t.begin_fill()
    t.circle(30)
    t.end_fill()

blue_square()
brown_square()
black_wheel()

turtle.done()
    