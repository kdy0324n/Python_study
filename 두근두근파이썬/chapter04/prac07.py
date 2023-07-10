import turtle
t = turtle.Turtle()
t.shape("turtle")

c = ["yellow","red","blue"]
t.fillcolor(c[0])
t.begin_fill()
t.circle(50)
t.end_fill()
t.up()
t.fd(100)
t.down()

t.fillcolor(c[1])
t.begin_fill()
t.circle(50)
t.end_fill()
t.up()
t.fd(100)
t.down()

t.fillcolor(c[2])
t.begin_fill()
t.circle(50)
t.end_fill()