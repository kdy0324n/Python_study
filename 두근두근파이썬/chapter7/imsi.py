# # def countVowel(string):
# #     v,c = 0,0
# #     for ch in string:
# #         if ch in ['a','e','i','o','u']:
# #             v+=1
# #         else :
# #             c+=1
# #     return v,c

# # s = input("문자열 입력:")
# # a,b = countVowel(s)
# # print(f"자음은{b}개, 모음은{a}개")

# def calculate_area(r):
#     global area 
#     area = 3.14 * r**2
#     return

# area=0
# calculate_area(5)
# print(area)

""" import random as rd
import turtle

t= turtle.Turtle()


def drawit(x,y):
    t.fillcolor(rd.random(),rd.random(),rd.random())
    t.up()
    t.goto(x,y)
    t.down()

    t.begin_fill()
    for i in range(4):
        t.fd(100)
        t.lt(90)
    t.end_fill()
    
s = turtle.Screen()
s.onscreenclick(drawit)
turtle.done() """


""" import turtle

def draw(x,y):
    t.goto(x,y)

t = turtle.Turtle()
s = turtle.Screen()
s.onscreenclick(draw)
s.onkey(t.penup,"Up")
s.onkey(t.pendown,"Down")
turtle.done() """

import turtle

def tree(length):
    if length>5:
        t.fd(length)
        t.rt(20)
        tree(length-15)
        t.lt(40)
        tree(length-15)
        t.rt(20)
        t.bk(length)

t = turtle.Turtle()
t.lt(90)


t.color("green")
t.speed(0)
tree(90)



