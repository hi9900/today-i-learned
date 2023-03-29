# 최대공약수 구하기
# 입력: a, b
# 출력: a와 b의 최대공약수

def gcd(a, b):
    i = min(a, b)
    while 1:
        if i == 1:
            return 1
        if a % i == b % i == 0:
            return i
        i -= 1


print(gcd(1, 5))    # 1
print(gcd(3, 6))    # 3
print(gcd(60, 24))  # 12
print(gcd(81, 27))  # 27


# 유클리드 알고리즘
def gcd_e(a, b):
    if b == 0:
        return a
    return gcd_e(b, a % b)


print(gcd_e(1, 5))    # 1
print(gcd_e(3, 6))    # 3
print(gcd_e(60, 24))  # 12
print(gcd_e(81, 27))  # 27