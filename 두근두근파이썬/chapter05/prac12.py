year = input("출생연도를 입력하시오: ")
t = int(year[3])
if t==0 or t==5:
    print("월요일에 접종가능합니다.")
elif t==1 or t== 6:
    print("화요일에 접종가능합니다.")
elif t==2 or t== 7:
    print("수요일에 접종가능합니다.")    
elif t==3 or t== 8:
    print("목요일에 접종가능합니다.")
elif t==4 or t== 9:
    print("금요일에 접종가능합니다.")