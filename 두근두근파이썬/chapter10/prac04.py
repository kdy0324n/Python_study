from tkinter import *
import random as rd
re = rd.randint(0,100)

def game():
    n = int(e.get())
    if n==re:
        Relb['text']="correct"
        #Relb.config(text="collect")
    elif n<re:
        Relb['text']="low"
        #Relb.config(text="low")
    else:
        Relb['text'] = "high"
        #Relb.config(text="high")

window = Tk()
window.geometry("500x300")
lb1 = Label(window,text="Gussing Game",font=20)
lb1.place(x=150,y=30,width=150)

e = Entry(window)
e.place(x=150,y=60,width=200)

btn1 = Button(window,text="guess",command=game)
btn2 = Button(window,text="reset")

btn1.place(x=150,y=100)
btn2.place(x=210,y=100)

Relb = Label(window,text="")
Relb.place(x=150,y=130)

window.mainloop()