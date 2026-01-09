# 최솟값 구하기
# 입력: 숫자가 n개 들어 있는 리스트
# 출력: 숫자 n개 중 최솟값
def find_min(lst):
    n = len(lst)
    minV = lst[0]
    for i in range(1, n):
        if lst[i] < minV:
            minV = lst[i]
    return minV


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_min(v))
