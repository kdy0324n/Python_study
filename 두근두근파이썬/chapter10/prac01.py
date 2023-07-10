from tkinter import *

window = Tk()
window.title("tk")

""" window.geometry("800,400")
window.resizable(width=False,height=False) """


lb1 = Label(text="이름")
lb2 = Label(text="직업")
lb3 = Label(text="국적")

lb1.grid(row=0,column=1)
lb2.grid(row=1,column=1)
lb3.grid(row=2,column=1)

e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)

e1.grid(row=0,column=3)
e2.grid(row=1,column=3)
e3.grid(row=2,column=3)

btn1 = Button(text="Show")
btn2 = Button(text="Quit")
btn1.grid(row=3,column=0)
btn2.grid(row=3,column=2)

window.mainloop()
