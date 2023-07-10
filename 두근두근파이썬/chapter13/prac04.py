from tkinter import *
import random
import time

class Ball:
    def __init__(self,canvas,color):
        self.canvas = canvas
        x1 = random.randint(10,50)
        y1 = random.randint(60,110)
        self.id = canvas.create_oval(x1,x1,y1,y1,fill=color)
        self.canvas.move(self.id,245,100)

        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = random.choice(starts)
        self.y = random.choice(starts)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = random.randint(1, 3)
        if pos[3] >= self.canvas_height:
            self.y = random.randint(-3, -1)
        if pos[0] <= 0:
            self.x = random.randint(1, 3)
        if pos[2] >= self.canvas_width:
            self.x = random.randint(-3, -1)

tk = Tk()
tk.title("tk")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()
tk.update()

color = ["red","pink","blue","yellow","orange","purple","navy"]

ball1  = Ball(canvas,random.choice(color))
ball2  = Ball(canvas,random.choice(color))
ball3  = Ball(canvas,random.choice(color))
ball4  = Ball(canvas,random.choice(color))
ball5  = Ball(canvas,random.choice(color))
ball6  = Ball(canvas,random.choice(color))
while 1:
    ball1.draw()
    ball2.draw()
    ball3.draw()
    ball4.draw()
    ball5.draw()
    ball6.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)