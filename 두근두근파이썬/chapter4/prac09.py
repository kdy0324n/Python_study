import turtle

t = turtle.Turtle()

list = [[100,100],[200,100],[200,200]]
color = ["red","yellow","red"]
t.shape("turtle")

t.stamp()

t.fillcolor(color[0])
t.goto(list[0][0],list[0][1])
t.stamp()

t.fillcolor(color[1])
t.goto(list[1][0],list[1][1])
t.stamp()

t.fillcolor(color[2])
t.goto(list[2][0],list[2][1])
t.stamp()
# for i in range(3):
#     t.fillcolor(color[i])
#     t.goto(list[i][0],list[i][1])
#     t.stamp()
turtle.done()
