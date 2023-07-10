from tkinter import *
import random as rd
window = Tk()

canvas = Canvas(window,width=500,height=500)
canvas.pack()
color = ["red","orange","yellow","green","blue","violet"]
for i in range(10):
    x = rd.randint(0,200)
    y = rd.randint(0,200)
    length = rd.randint(20,50)
    canvas.create_oval(x,y,x+length,y+length,fill=rd.choice(color))
window.mainloop()