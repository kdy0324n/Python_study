from tkinter import *

window = Tk()
window.geometry("500x300")
idx=1

def fuc():
    global idx
    s=""    
    s+="[ #"+str(idx)+"] "
    s += e1.get()
    s+="\n"
    
    textarea.insert(INSERT,s)
    idx+=1

lb1 = Label(window,text="할일을 입력하세요")
lb1.place(x=50,y=10)

e1 = Entry(window,width=25)
e1.place(x=10,y=30)

btn = Button(window,text="추가",command=fuc)
btn.place(x=60,y=50)

textarea = Text(window,height=5,width=25,font=("Arial",15))
textarea.place(x=10,y=70)



window.mainloop()