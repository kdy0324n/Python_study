import time

pt = True
st = time.time()
#print("30초가 지나시작")
input("30초가 지나면 엔터키를 누르세요")

et = time.time()
t = et-st

print(f"{30-t}초가 빨랐습니다")