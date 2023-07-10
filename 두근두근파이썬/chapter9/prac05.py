problem = {"파이썬":"최근에 가자 떠오르는 프로그래밍 언어","변수":"데이터 저장 메모리 공간",
           "함수":"작업을 수행하는 문장들의 집합에 이름을 붙인것","리스트":"서로 관련이 없는 항목들의 모임"}

for word in problem.keys():
    print(problem[word])
    print("(1)파이썬 (2) 변수 (3) 함수 (4) 리스트")
    ans = input()
    if ans==word:
        print("정답입니다!")
    else:
        print("틀렸습니다.")
    