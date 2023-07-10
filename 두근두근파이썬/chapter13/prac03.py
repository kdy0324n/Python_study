import turtle

class T():
    def __init__(self,shape,head):
        self.t = turtle.Turtle()
        self.t.shape(shape)
        self.t.setheading(head)
    def move(self):
        self.t.forward(100)


t1 = T("turtle",0)
t2 = T("circle",180)

t1.move()
t2.move()

turtle.done()