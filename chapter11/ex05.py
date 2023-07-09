inputfile=input("입력 파일 이름: ")
outputfile = input("출력 파일 이름: ")
input_route = "C:/Users/kdy03/OneDrive/바탕 화면/파이썬/chapter11/"+inputfile  # 파일 경로
output_route = "C:/Users/kdy03/OneDrive/바탕 화면/파이썬/chapter11/"+outputfile  # 파일 경로

infile = open(input_route,"r")
F = infile.readlines()
infile.close()

sum = 0
for i in F:
    sum+=float(i.rstrip())
avg = sum/len(F)
 
outfile = open(output_route,"w",encoding="utf-8")
outfile.write(f"합계={str(sum)}\n")
outfile.write(f"평균={str(avg)}")
