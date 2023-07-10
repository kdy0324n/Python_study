import turtle
t = turtle.Turtle()
t.shape('turtle')

r =  50
t.circle(r)
t.up()
t.goto(100,0)
t.down()

r+=20
t.circle(r)
t.up()
t.goto(200,0)
t.down()
r+=20
t.circle(r)

