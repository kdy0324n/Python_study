import random as rd

cnt=[0,0,0,0,0,0]
for i in range(200):
    v = rd.randint(0,5)
    cnt[v]+=1
for i in range(6):
    print(f"주사위가 {i+1} 인 경우는 {cnt[i]}번")