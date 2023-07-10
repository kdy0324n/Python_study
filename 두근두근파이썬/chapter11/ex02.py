s = input("파일 이름을 입력하시오: ")
route = "C:/Users/kdy03/OneDrive/바탕 화면/파이썬/chapter11/"  # 파일 경로
route += s
infile = open(route, "r", encoding="utf-8")
ss = input("삭제할 문자열을 입력하시오: ")

st = infile.read()
infile.close()

st = st.replace(ss, '') 

outfile = open(route, "w", encoding="utf-8")
outfile.write(st)
outfile.close()
