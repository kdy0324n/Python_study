s = input("파일 이름: ")
route = "C:/Users/kdy03/OneDrive/바탕 화면/파이썬/chapter11/"  # 파일 경로
route+=s
infile = open(route,"r")
n = int(input("줄번호: "))

s = infile.readlines()
print()
if len(s)<n:
    print("해당 줄번호가 너무 큽니다.")
else:
    line = s[n-1]
    line.rstrip()
    print(f"{n}번째 줄: {line}")


infile.close()