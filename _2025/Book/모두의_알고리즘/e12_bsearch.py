# 리스트에서 특정 숫자 위치 찾기(이분 탐색과 재귀 호출)
# 입력: 리스트 a, 찾는 값 x
# 출력: 특정 숫자를 찾으면 그 값의 위치, 찾지 못하면 -1

# 리스트 a의 어디부터(start) 어디까지(end)가 탐색 범위인지 지정하여
# 그 범위 안에서 x를 찾는 재귀 함수
def binary_search_sub(lst, target, start, end):
    if start > end:
        return -1

    mid = (start+end) // 2
    if target == lst[mid]:
        return mid
    elif target > lst[mid]:
        return binary_search_sub(lst, target, mid+1, end)
    else:
        return binary_search_sub(lst, target, start, mid-1)


# 리스트 전체(0 ~ len(a)-1)를 대상으로 재귀 호출 함수 호출
def binary_search(a, x):
    return binary_search_sub(a, x, 0, len(a) - 1)


d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36))
print(binary_search(d, 50))

