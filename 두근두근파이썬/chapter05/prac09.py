import random as rd
num = rd.randint(0,99)
n = int(input("복권번호를 입력하시오(0에서 99사이): "))
print("당첨번호는 %d 입니다."%num)
if num%10==n%10 and num//10==n//10:
    print("상금은 100만원입니다.")
elif num%10==n%10 or num//10==n//10:
    print("상금은 50만원입니다.")
else:
    print("상금은 없습니다.")