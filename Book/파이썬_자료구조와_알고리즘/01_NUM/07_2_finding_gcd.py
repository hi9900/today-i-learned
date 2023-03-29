# 1.7.2 최대공약수

def finding_gcd(a, b):
    while b != 0:
        result = b
        a, b = b, a % b
    return result

num1, num2 = 21, 12
print(finding_gcd(num1, num2))  # 3