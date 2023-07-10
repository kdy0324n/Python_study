arr = {}
for i in range(65,65+26):
    arr[chr(i)]=0
for i in range(97,97+26):
    arr[chr(i)]=0
s = input("입력 파일 이름: ")
route = "C:/Users/kdy03/OneDrive/바탕 화면/파이썬/chapter11/"  # 파일 경로
route += s
infile = open(route,"r")
F = infile.read()
for i in F:
    if i=='\n':
        continue
    arr[i]+=1
print(arr)
infile.close()