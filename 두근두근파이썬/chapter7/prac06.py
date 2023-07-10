def getGrade(score):
    if score>=90:
        return 'A'
    elif score>=80:
        return 'B'
    elif score>=70:
        return 'C'
    elif score>=60:
        return 'D'
    else:
        return 'E'
score = int(input("성적을 입력하시오: "))
print(f"학점은 {getGrade(score)}입니다.")