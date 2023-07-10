route = "C:/Users/kdy03/OneDrive/바탕 화면/파이썬/chapter11/"#파일 경로
s = input("파일의 이름을 입력하세요: ")
route+=s
infile = open(route,"r")
print(f"파일 안에는 총 {len(infile.read())} 개의 글자가 있습니다.")
infile.close()
