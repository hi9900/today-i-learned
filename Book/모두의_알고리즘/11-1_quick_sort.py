# 쉽게 설명한 퀵 정렬
# 입력: 리스트 a
# 출력: 정렬된 새 리스트
def quick_sort(a):
    n = len(a)

    if n <= 1:
        return a

    # 기준 값에 맞춰 그룹을 정렬
    # 리스트의 마지막 값을 기준 값으로
    pivot = a[-1]
    g1 = []
    g2 = []
    # 마지막 값은 기준 값이므로 n-1
    for i in range(n-1):
        if a[i] < pivot:
            g1.append(a[i])
        else:
            g2.append(a[i])

    # 기준 값과 합쳐 하나의 리스트로 반환
    return quick_sort(g1) + [pivot] + quick_sort(g2)


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(quick_sort(d))
