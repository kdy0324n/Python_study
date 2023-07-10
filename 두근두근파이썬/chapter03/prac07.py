num = int(input("정수를 입력하시오: "))
re = 0
re+=num%10
num/=10
re+=num%10
num/=10
re+=num%10
num/=10
re+=num%10
num/=10

print("자리수의 합: %d"%re)