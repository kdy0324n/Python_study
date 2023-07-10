import turtle
def draw_line():
    t = turtle.Turtle()
    t.shape("turtle")
    for i in range(8):
        t.fd(100)
        t.bk(100)
        t.lt(360/8)
    turtle.done()
draw_line()
