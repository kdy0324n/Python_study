d = {}

while 1:
    a = input("(입력모드)이름을 입력하시오:")
    if a=="":
        k = input("(검색모드)이름을 입력하시오: ")
        print(d[k])
        continue
    phone = input("전화번호를 입력하시오:")
    d[a]=phone