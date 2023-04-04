# 최댓값 구하기
# 입력: 숫자가 n개 들어 있는 리스트
# 출력: 숫자 n개 중 최댓값
def find_max(lst, n):
    if n == 1:
        return lst[0]

    # n-1 개 중 최댓값 vs n-1번째 위치 값
    max_v = find_max(lst, n-1)
    if max_v > lst[n-1]:
        return max_v
    else:
        return lst[n-1]


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(v, len(v)))  # 함수에 리스트의 자료 갯수를 인자로 추가하여 호출
