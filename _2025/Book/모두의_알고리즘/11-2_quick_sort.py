# 퀵 정렬
# 입력: 리스트 a
# 출력: 없음(입력으로 주어진 a가 정렬됨)
# 리스트 a의 어디부터(start) 어디까지(end)가 정렬 대상인지
# 범위를 지정하여 정렬하는 재귀 호출 함수
def quick_sort_sub(a, start, end):
    # 정렬 대상이 1개 이하면 리턴
    if end - start <= 0:
        return

    # 리스트의 마지막 값을 기준값으로
    pivot = a[end]
    i = start
    for j in range(start, end):
        # 기준값보다 작으면 왼쪽으로
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    # 기준 값 = a[i] 위치로
    a[i], a[end] = a[end], a[i]

    # 기준 값보다 작은 값 재귀
    quick_sort_sub(a, start, i-1)
    # 기준 값보다 큰 값 재귀
    quick_sort_sub(a, i+1, end)


# 리스트 전체(0 ~ len(a)-1)를 대상으로 재귀 호출 함수 호출
def quick_sort(a):
    quick_sort_sub(a, 0, len(a) - 1)


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
quick_sort(d)
print(d)
