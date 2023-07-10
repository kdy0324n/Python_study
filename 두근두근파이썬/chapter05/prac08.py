n = int(input("강아지의 나이를 입력하시오: "))
re = 0
if n>=2:
    re+=20
    n-=2
elif n==1:
    re+=10
    n-=1

re += 4*n
print("강아지의 나이를 사람 나이로 환산하면 %d 살 입니다."%re)

