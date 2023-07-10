import random as rd

list = []
for i in range(26):
    list.append(chr(i+97))
for i in range(10):
    list.append(i)
re = ""
re +=str(rd.choice(list))
re +=str(rd.choice(list))
re +=str(rd.choice(list))
print(re)