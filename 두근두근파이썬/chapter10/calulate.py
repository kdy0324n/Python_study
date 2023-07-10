from tkinter import *



window = Tk()
window.title("My calculator")
display = Entry(window,width=33,bg="yellow")
display.grid(row=0,column=0,columnspan=5)

btn_list = [
    '7','8','9','/','c',
    '4','5','6','*',' ',
    '1','2','3','-',' ',
    '0','.','=','+',' '
]

def click(key):
    if key=="=":
        result = eval(display.get())
        s = str(result)
        display.insert(END,"="+s)
    elif key=="c":

        display.delete(0,len(display.get()))
    else:  
        display.insert(END,key)

rowidx = 1
colidx = 0
for btn_text in btn_list:
    def process(t=btn_text):
        click(t)
    Button(window,text=btn_text,width=5,command=process).grid(row=rowidx,column=colidx)
    colidx+=1
    if colidx > 4:
        rowidx+=1
        colidx = 0
window.mainloop()