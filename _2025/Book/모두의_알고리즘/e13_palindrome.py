# 주어진 문장이 회문인지 확인(문자열의 앞뒤를 서로 비교)
# 입력: 문자열 s
# 출력: 회문이면 True, 아니면 False
def palindrome(s):
    i = 0
    j = len(s)-1
    while i < j:
        if not s[i].isalpha():
            i += 1
        elif not s[j].isalpha():
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
    return True


print(palindrome("Wow"))
print(palindrome("Madam, I’m Adam."))
print(palindrome("Madam, I am Adam."))
