h = int(input("키를 입력하시오(cm): "))
w = int(input("몸무게를 입력하시오(kg): "))
h*=0.01
bmi = w/h**2
print(f"당신의 bmi = {bmi}")

if bmi<=18.4:
    print("저체중")
elif bmi<=24.9:
    print("적정 체중")
else:
    print("과체중")