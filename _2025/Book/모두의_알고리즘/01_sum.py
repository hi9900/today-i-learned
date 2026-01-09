# 1부터 n까지 연속한 숫자의 합을 구하는 알고리즘 1
# 입력: n
# 출력: 1부터 n까지의 숫자를 더한 값

# 변수 n을 입력받아 1부터 n까지 연속한 숫자의 합을 반환하는 함수
def sum_n(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s


print(sum_n(10))    # 55
print(sum_n(100))   # 5050

# 1부터 n까지 연속한 숫자의 합을 구하는 알고리즘 2
# 입력: n
# 출력: 1부터 n까지의 숫자를 더한 값

# 가우스 방법
def sum_n(n):
    return n*(n+1)/2


print(sum_n(10))    # 55
print(sum_n(100))   # 5050