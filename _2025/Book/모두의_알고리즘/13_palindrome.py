# 주어진 문장이 회문인지 아닌지 찾기(큐와 스택의 특징을 이용)
# 큐와 스택에서 차례로 꺼낸 값이 모두 같으면 회문
# 입력: 문자열 s
# 출력: 회문이면 True, 아니면 False
def palindrome(s):
    queue = []
    stack = []
    
    # 알파벳을 모두 큐와 스택에 넣음
    for c in s:
        # 문자가 알파벳이면 (공백, 숫자, 특수문자가 아니면)
        if c.isalpha():
            # 그 문자의 소문자를 추가
            queue.append(c.lower())
            stack.append(c.lower())

    # 큐와 스택에 있는 문자를 꺼내면서 비교
    # 문자가 남아 있는 동안 꺼냄
    while queue:
        # 다르면 회문이 아님
        if queue.pop(0) != stack.pop():
            return False

    return True


print(palindrome("Wow"))
print(palindrome("Madam, I’m Adam."))
print(palindrome("Madam, I am Adam."))
