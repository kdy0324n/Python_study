import turtle 
t = turtle.Turtle()

def f(x):
    t.color("red")
    for i in range(150):
        t.goto(i,(i**2+1)*0.01)

t.shape('turtle')
t.fd(200)
t.bk(200)
t.lt(90)
t.fd(200)
t.bk(200)
f(150)

turtle.done()

