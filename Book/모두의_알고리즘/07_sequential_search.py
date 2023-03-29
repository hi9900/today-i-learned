# 리스트에서 특정 숫자의 위치 찾기
# 입력: 리스트 a, 찾는 값 x
# 출력: 찾으면 그 값의 위치, 찾지 못하면 -1

def search_list(a, x):
    n = len(a)
    for i in range(n):
        if x == a[i]:
            return i
    return -1


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18))  # 2(순서상 세 번째지만, 위치 번호는 2)
print(search_list(v, 33))  # 3(33은 리스트에 두 번 나오지만 처음 나온 위치만 출력)
print(search_list(v, 900))  # -1(900은 리스트에 없음)