import turtle


t = turtle.Turtle()
t.speed(0)
t.shape("turtle")
t.color('red','yellow')
t.begin_fill()
while True:
    t.fd(200)
    t.lt(170)
    print(int(abs(t.pos())))
    if abs(t.pos())<1:
        break
t.end_fill()

turtle.done()