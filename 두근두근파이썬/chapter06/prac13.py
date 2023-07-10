import turtle
t = turtle.Turtle()
t.shape('turtle')
t.pensize(20)
colors = ["red","orange","yellow","green","blue","indigo","violet"]
for i in range(7):
    t.up()
    t.goto(30+i*30,0)
    t.down()
    t.setheading(90)
    t.color(colors[i])
    t.circle(30+i*30,180)
t.done()
