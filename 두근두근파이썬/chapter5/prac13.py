import random as rd

r = rd.randint(0,2)#0 가위 1 바위 2 보
l = ["가위","바위","보"]
u = input("가위, 바위, 보를 입력하시오: ")
print(f"컴퓨터: {l[r]}")
c = l[r]

if u=="가위":
    if c=="가위":
        print("비겼습니다")
    elif c=="바위":
        print("컴퓨터가 이겼습니다.")
    else:
        print("컴퓨터가 졌습니다.")
elif u=="바위":
    if c=="가위":
        print("컴퓨터가 졌습니다.")
    elif c=="바위":
        print("비겼습니다.")
    else:
        print("컴퓨터가 이겼습니다.")
else:
    if c=="가위":
        print("컴퓨터가 이겼습니다.")
    elif c=="바위":
        print("컴퓨터가 졌습니다.")
    else:
        print("비겼습니다.")
