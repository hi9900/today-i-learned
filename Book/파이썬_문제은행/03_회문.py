# 단어를 입력했을 때 해당 단어가 회문인지 판단하는 프로그램을 작성해주세요.

def is_palin(word):
    if word == word[::-1]:
        return f"{word}는 회문입니다."
    return f"{word}는 회문이 아닙니다."


word = input("단어를 입력해주세요: ")
print(is_palin(word))