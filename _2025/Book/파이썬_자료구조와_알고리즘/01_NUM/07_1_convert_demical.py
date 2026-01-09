# 1.7.1 진법 변환

# 다른 진법의 숫자를 10진법으로
def convert_to_demical(number, base):
    multiplier, result = 1, 0
    while number > 0:
        result += number % 10 * multiplier
        multiplier *= base
        number = number // 10
    return result

number, base = 1001, 2      # 9
print(convert_to_demical(number, base))

# 10진수를 다른 진법으로 변환
def convert_from_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0:
        result += number % base * multiplier
        multiplier *= 10
        number = number // base
    return result

number, base = 9, 2     # 1001
print(convert_from_decimal(number, base))

# base가 10보다 큰 경우, 문자를 사용해야 한다.
# A는 10, B는 11, C는 12, ...
# 10진법 숫자를 20이하의 진법으로 변환
def convert_from_decimal_larger_bases(number, base):
    strings = "0123456789ABCDEFGHIJ"
    result = ""
    while number > 0:
        digit = number % base
        result = strings[digit] + result
        number = number // base
    return result

number, base = 31, 16   # 1F
print(convert_from_decimal_larger_bases(number, base))

# 재귀함수를 사용한 진법 변환
def convert_dec_to_any_base_rec(number, base):
    convertString = "0123456789ABCDEF"
    if number < base:
        return convertString[number]
    else:
        return convert_dec_to_any_base_rec(number // base, base) \
            + convertString[number % base]

number, base = 9, 2     # 1001
print(convert_dec_to_any_base_rec(number, base))
    