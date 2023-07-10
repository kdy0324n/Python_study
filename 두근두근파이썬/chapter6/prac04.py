m = 1000
i=0
while True:
    if m>=2000:
        print(f"{i} 년이 걸립니다.")
        break
    i+=1
    m+=m*0.07
    print(f"{i}년후 {m}가 되었습니다.")
    
