num1  = int(input("첫 번째 숫자를 입력하시오: "))
num2  = int(input("두 번째 숫자를 입력하시오: "))
num3  = int(input("세 번째 숫자를 입력하시오: "))
if num1>num2 and num1>num3:
    print("가장 큰 숫자는 %d입니다"%num1)
elif num2>num1 and num2>num3:
    print("가장 큰 숫자는 %d입니다"%num2)
else:
    print("가장 큰 숫자는 %d입니다"%num3)
