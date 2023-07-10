import turtle
t = turtle.Turtle()
t.shape('turtle')

t.width(6)
radius = 50
t.speed(10)
idx = [[-110,0],[0,0],[110,0],[-55,-50],[55,-50]]
color = ['blue','black','red','yellow','green']

for i in range(5):
    t.color(color[i])
    t.penup()
    t.goto(idx[i][0],idx[i][1])
    t.pendown()
    t.circle(radius)
turtle.done()