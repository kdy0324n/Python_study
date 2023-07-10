import random

s = "abcdefghijklmnopqrstuvwxyz"
num="0123456789"

ans=""

for i in range(3):
    ans+=random.choice(s)
for i in range(2):
    ans+=random.choice(num)
print(ans)

#186페이지