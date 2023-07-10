def sumProblem(x,y):
    return x+y


num1 = int(input("첫 번째 정수 "))
num2 = int(input("두 번째 정수 "))
num3 = int(input(f"정수 {num1}+{num2}의 합은? "))
if num3==sumProblem(num1,num2):
    print("정답입니다.")
else:
    print("틀렸습니다.")
