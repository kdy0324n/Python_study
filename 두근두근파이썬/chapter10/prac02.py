from tkinter import *

window = Tk()

def fuc():
    t = float(e1.get())
    t*=1.609
    t=int(t)
    e2.insert(0,str(t)+"km")

lb1 = Label(window,text="마일:")
lb2 = Label(window,text="킬로미터:")
lb1.place(x=20,y=20)
lb2.place(x=20,y=40)

e1 = Entry(window)
e2 = Entry(window)
e1.place(x=80,y=20)
e2.place(x=80,y=40)

btn1 = Button(window,text="변환",command=fuc)
btn1.place(x=20,y=60,width=60)
window.mainloop()
