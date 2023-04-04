# 리스트에서 특정 숫자 위치 전부 찾기
# 입력: 리스트 a, 찾는 값 x
# 출력: 찾는 값의 위치 번호가 담긴 리스트, 찾는 값이 없으면 빈 리스트 []
def search_list(a, x):
    n = len(a)
    result = []
    for i in range(n):
        if a[i] == x:
            result.append(i)

    return result


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18))   # [2]    (순서상 세 번째지만, 위치 번호는 2)
print(search_list(v, 33))   # [3, 6] (33은 리스트에 두 번 나옴)
print(search_list(v, 900))  # []     (900은 리스트에 없음)
