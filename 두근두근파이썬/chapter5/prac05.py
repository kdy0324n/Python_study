import random as rd

num1 = rd.randint(1,100)
num2 = rd.randint(1,100)
print(f"{num1}-{num2}=",end="")
num3 = int(input(""))
if num3==num1-num2:
    print("맞았습니다")
else:
    print("틀렸습니다.")