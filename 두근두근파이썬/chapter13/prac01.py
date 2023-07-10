class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calcPerimeter(self):
        self.calcperimeter = 3.141592 * 2 * self.radius
    def calcArea(self):
        self.calcarea = 3.141592 * self.radius**2
    def __str__(self):
        msg = "반지름: "+str(self.radius) +"\n원의 면적: "+str(self.calcarea) +"\n원의 둘레: "+str(self.calcperimeter)
        return msg

myCircle = Circle(100)
myCircle.calcPerimeter()
myCircle.calcArea()
print(myCircle)