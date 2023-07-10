import turtle
t = turtle.Turtle()
t.shape('turtle')

list = [ [-80,0],[0,0],[80,0]]
list2 = [[-40,-40],[40,-40]]

for i in list:
    t.up()
    t.goto(i[0],i[1])
    t.down()
    t.circle(50)
for i in list2:
    t.up()
    t.goto(i[0],i[1])
    t.down()
    t.circle(50)
turtle.done()
