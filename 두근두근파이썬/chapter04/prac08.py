import turtle

t = turtle.Turtle()
t.shape("turtle")
list=[[0,0],[100,100],[200,100]]

t.goto(list[0][0],list[0][1])
t.goto(list[1][0],list[1][1])
t.goto(list[2][0],list[2][1])
# for i in list:
#     t.goto(i[0],i[1])
turtle.done()
