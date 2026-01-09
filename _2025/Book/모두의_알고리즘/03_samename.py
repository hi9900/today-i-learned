# 두 번 이상 나온 이름 찾기
# 입력: 이름이 n개 들어 있는 리스트
# 출력: 이름 n개 중 반복되는 이름의 집합

def find_same_name(a):
    n = len(a)
    result = set()
    for i in range(n):
        for j in range(i+1, n):
            if a[i] == a[j]:
                result.add(a[i])
    return result


# 대소문자 유의: 파이썬은 대소문자를 구분함
name = ["Tom", "Jerry", "Mike", "Tom"]
print(find_same_name(name))     # {'Tom'}

name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(find_same_name(name2))    # {'Mike', 'Tom'}

