x1 = 0
y1 = 0
x2 = 100
y2 = 100

print(((x1-x2)**2 + (y1-y2)**2)**0.5)

xy = ((x1-x2)**2 + (y1-y2)**2)**0.5
#9번
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.setheading(45)
t.fd(141)
t.bk(141)
t.setheading(0)
t.fd(100)
t.lt(90)
t.fd(100)
turtle.done()

#10번
'''import turtle
t = turtle.Turtle()

t.width(3)
t.setheading(45)
t.fd(xy)

t.write("점의 길이"+str(xy))

turtle.done()'''