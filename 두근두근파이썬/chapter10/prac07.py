from tkinter import *
import random as rd
window = Tk()

user_score = 0
computer_score = 0

computer=1#1은 주먹 2가위 3은 보
user=1

def Rdchoice():
    global computer
    computer = rd.randint(1,3)

def Result():
    global user
    global user_score
    global computer
    global computer_score
    s="비겼습니다"
    if user==1:
        if computer==1:
            s="비겼습니다."
        if computer==2:
            s="사용자 승리!!" 
            user_score+=1
        if computer==3:
            s="컴퓨터 승리!!"
            computer_score+=1
    elif user==2:
        if computer==1:
            s="컴퓨터 승리!!"
            computer_score+=1
        if computer==2:
            s="비겼습니다."
        if computer==3:
            s="사용자 승리!!"
            user_score+=1
    else:
        if computer==1:
            s="사용자 승리!!"
            user_score+=1
        if computer==2:
            s="컴퓨터 승리!!"
            computer_score+=1
        if computer==3:
            s="비겼습니다."
    a = "사용자 점수: "+str(user_score)
    b = "컴퓨터 점수: "+str(computer_score)
    c = "사용자="+str(user)+", 컴퓨터="+str(computer)+" "+s
    userlb.config(text=a)
    computerlb.config(text=b)
    relb.config(text=c)

def rock():
    Rdchoice()
    global user
    user = 1
    Result()

def scissors():
    Rdchoice()
    global user
    user = 2
    Result()

def paper():
    Rdchoice()
    global user
    user = 3
    Result()

lb1 = Label(window,text="가위 바위 보 게임",fg="blue")
lb1.pack(side="top")
f = Frame(window)
btn1 = Button(f,text="바위",width=20,background="orange",command=rock)
btn2 = Button(f,text="가위",width=20,bg="yellow",command=scissors)
btn3 = Button(f,text="보",width=20,bg="skyblue",command=paper)
f.pack(side="top")
btn1.grid(row=0,column=0,padx=50)
btn2.grid(row=0,column=1,padx=50)
btn3.grid(row=0,column=2,padx=50)

userlb = Label(window,text="사용자 점수: 0")
computerlb = Label(window,text="컴퓨터 점수: 0")
relb = Label(window,text="",fg="orange")

userlb.pack(side="top")
computerlb.pack(side="top")
relb.pack(side="top")

window.mainloop()
