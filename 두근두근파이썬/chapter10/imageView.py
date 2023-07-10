""" from tkinter import *

def change_img():
    path = inputBox.get()
    img = PhotoImage(file=path)
    imageLabel.configure(image=img)
    imageLabel.image = img

window = Tk()


photo = PhotoImage(file="C:/Users/kdy03/Desktop/프로그래밍기초_파이썬/두근두근파이썬/chapter10/hair.gif")
imageLabel = Label(window,image=photo)
imageLabel.pack()

inputBox = Entry(window)
inputBox.pack()

button = Button(window,text='Submit',command=change_img)
button.pack()

window.mainloop() """

from tkinter import *

window = Tk()
Img = "C:/Users/kdy03/Desktop/프로그래밍기초_파이썬/두근두근파이썬/chapter10/hair.gif"
window.title("3*2격자배치")
window.geometry("900x600")
window.resizable(width=False,height=False)

p1 = PhotoImage(file=Img)
p2 = PhotoImage(file=Img)
p3 = PhotoImage(file=Img)
p4 = PhotoImage(file=Img)
p5 = PhotoImage(file=Img)
p6 = PhotoImage(file=Img)
a = Label(window,image=p1)
b = Label(window,image=p2)
c = Label(window,image=p3)
d = Label(window,image=p4)
e = Label(window,image=p5)
f = Label(window,image=p6)

a.grid(row=0,column=0)
b.grid(row=0,column=1)
c.grid(row=0,column=2)

d.grid(row=1,column=0)
e.grid(row=1,column=1)
f.grid(row=1,column=2)

window.mainloop()





