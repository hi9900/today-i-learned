# 선택 정렬
# 입력: 리스트 a
# 출력: 없음(입력으로 주어진 a가 정렬됨)

def sel_sort(a):
    n = len(a)
    for i in range(n-1):
        min_i = i
        for j in range(i, n):
            if a[j] < a[min_i]:
                min_i = j
        a[i], a[min_i] = a[min_i], a[i]


d = [2, 4, 5, 1, 3]
sel_sort(d)
print(d)
