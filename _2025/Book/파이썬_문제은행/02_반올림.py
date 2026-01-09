# 파이썬에 내장된 round() 함수를 이용하지 않고,
# 반올림 계산을 실행할 수 있는 코드를 작성해보세요.

# 조건 1 : 소수 첫째 자리에서 반올림이 이루어집니다. (ex. 3.14 → 3, 1.5 → 1)
# 조건 2 : 소수 첫째 자리가 0~4이면 버림, 5~9이면 올림을 합니다.

def no_round(x):
    if len(x) == 1:
        return int(x[0])

    if int(x[1]) >= 5:
        return int(x[0]) + 1

    return int(x[0])


num = input("숫자를 입력해주세요: ").split(".")
print(no_round(num))
