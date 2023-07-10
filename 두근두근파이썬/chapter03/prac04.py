a = int(input("이자율(단위: %): "))
b = int(input("원금(단위: 만원): "))
c = int(input("거치 기간(단위: 년): "))

for i in range(c):
    b+=b*0.05
b*=10000
b = round(b)
print("%d"%b)