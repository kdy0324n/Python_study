# import turtle
# t = turtle.Turtle()
# t.shape('turtle')
# n = int(turtle.textinput('크기입력',''))

# t.color('red')
# t.begin_fill()
# for i in range(3):
#     t.fd(n)
#     t.lt(120)
# t.end_fill()
# t.rt(90)

# t.color('blue')
# t.begin_fill()
# for i in range(4):
#     t.fd(n)
#     t.lt(90)
# t.end_fill()

# turtle.done()
import webbrowser

url = input("url입력:")
webbrowser.open("https://www."+url+".com")
