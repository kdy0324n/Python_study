from tkinter import *

window = Tk()

def move_left():    
    x = -10
    y=0
    canvas.move(shape,x,y)
def move_right():    
    x = 10
    y=0
    canvas.move(shape,x,y)
def move_up():    
    x = 0
    y=-10
    canvas.move(shape,x,y)
def move_down():    
    x = 0
    y=10
    canvas.move(shape,x,y)

window.geometry("500x400")
canvas = Canvas(window,width=500,height=300,background="white")
shape=canvas.create_rectangle(200,100,250,150,fill="blue")
canvas.pack()

left_btn = Button(window,text="<-(left)",command=move_left)
right_btn = Button(window,text="->(right)",command=move_right)
up_btn = Button(window,text="^(up)",command=move_up)
down_btn = Button(window,text="v(down)",command=move_down)

left_btn.place(x=50,y=350)
right_btn.place(x=150,y=350)
up_btn.place(x=250,y=350)
down_btn.place(x=350,y=350)

window.mainloop()