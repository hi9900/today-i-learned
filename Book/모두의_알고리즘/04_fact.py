# 연속한 숫자의 곱을 구하는 알고리즘
# 입력: n
# 출력: 1부터 n까지 연속한 숫자를 곱한 값

def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


print(fact(1))
print(fact(5))
print(fact(10))


def fact_rec(n):
    if n <= 1:
        return 1
    return n * fact_rec(n-1)


print(fact_rec(1))
print(fact_rec(5))
print(fact_rec(10))