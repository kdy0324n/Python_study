x1 = int(input("큰 원의 중심좌표 x1: "))
y1 = int(input("큰 원의 중심좌표 y1: "))
r1 = int(input("큰 원의 반지름: "))

x2 = int(input("큰 원의 중심좌표 x2: "))
y2 = int(input("큰 원의 중심좌표 y2: "))
r2 = int(input("큰 원의 반지름: "))

dis = ((x1 - x2)**2 + (y1-y2)**2)**0.5
if dis+r2<r1:
    print("작은원이 큰원에 포함됩니다.")
elif dis<r1 + r2:
    print("작은원이 큰원에 걸칩니다.")
else:
    print("작은원이 큰 원에 포함되지 않습니다.")