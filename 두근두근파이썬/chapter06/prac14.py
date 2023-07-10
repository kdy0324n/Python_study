import turtle

t = turtle.Turtle()

t.pensize(20)


t.up()
t.goto(-250,250)
t.down()
def fuc():
    t.fd(200)
    t.rt(90)
    t.fd(30)
    t.rt(90)
    t.fd(200)
    t.lt(90)
    t.fd(30)
    t.lt(90)
for i in range(5):
    fuc()
turtle.done()