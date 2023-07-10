from tkinter import * 

window = Tk()

route = "C:/Users/kdy03/OneDrive/바탕 화면/파이썬/chapter11/ex07.txt"  # 파일 경로


readflie = []
idx = 0

def init():
    n1 = e1.get()
    e1.delete(0,len(n1))
    e2.delete(0,len(e2.get()))

def Append():
    init()    
    print("추가")
    f = open(route,"a",encoding="utf-8")
    f.write(f"\n{e1.get()} {e2.get()}")
    f.close()
def Show(idx):
    line = readflie[idx]
    line = line.replace("\n","")
    line = line.split(" ")
    
    e1.insert(0,line[0])
    e2.insert(0,line[1])
def First():
    init()
    print("처음")
    global idx
    idx = 0
    Show(idx)
def Next():
    global idx
    print("다음")
    if len(readflie)-1==idx : return
    init()
    idx +=1
    Show(idx)
def Begin():
    global idx
    print("이전")
    if 0==idx : return
    init()
    idx -=1
    Show(idx)
def Last():
    init()
    print("마지막")
    global idx
    idx = len(readflie)-1
    Show(idx)

def FileRead():
    print("파일읽기")
    global route
    global readflie
    infile = open(route,"r",encoding="utf-8")#한글 읽을때 주의
    #print(infile.readlines())
    readflie = infile.readlines()
    #s = infile.readlines()
    infile.close()



f1 = Frame(window)
f2 = Frame(window)
f3 = Frame(window)

lbname = Label(f1,text="이름")
lbphone = Label(f2,text="전화번호")

e1 = Entry(f1,width=20)
e2 = Entry(f2,width=20)

btn1 = Button(f3,text="추가",command=Append)
btn2 = Button(f3,text="처음",command=First)
btn3 = Button(f3,text="다음",command=Next)
btn4 = Button(f3,text="이전",command=Begin)
btn5 = Button(f3,text="마지막",command=Last)
btn6 = Button(f3,text="파일읽기",command=FileRead)

lbname.pack(side="left")
e1.pack(side="left")

lbphone.pack(side="left")
e2.pack(side="left")

btn1.pack(side="left")
btn2.pack(side="left")
btn3.pack(side="left")
btn4.pack(side="left")
btn5.pack(side="left")
btn6.pack(side="left")

# lbname.grid(row=0,column=0)
# lbphone.grid(row=1,column=0)

# e1.grid(row=0,column=1)
# e2.grid(row=1,column=1)

f1.pack()
f2.pack()
f3.pack()

# btn1.pack(side=LEFT)
# btn2.pack(side=LEFT)
# btn3.pack(side=LEFT)
# btn4.pack(side=LEFT)
# btn5.pack(side=LEFT)
# btn6.pack(side=LEFT)

# btn1.grid(row=2,column=0)
# btn2.grid(row=2,column=1)
# btn3.grid(row=2,column=2)
# btn4.grid(row=2,column=3)
# btn5.grid(row=2,column=4)
# btn6.grid(row=2,column=5)

window.mainloop()
