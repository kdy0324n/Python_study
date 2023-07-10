d = {}

d['one'] = "하나"
d['two'] = "둘"
d['three'] = "셋"

while 1 :
    q = input("")
    if q=="q":
        break
    if q not in d:
        print("nothing")
        continue
    
    print(d[q])