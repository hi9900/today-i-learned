# 내림차순 선택 정렬
# 입력: 리스트 a
# 출력: 없음(입력으로 주어진 a가 정렬됨)
def sel_sort(a):
    # 처리 범위의 최솟값을 찾아 그 값과 범위의 맨 앞에 있는 값을 서로 바꾸기
    n = len(a)
    for i in range(n-1):
        max_i = i
        for j in range(i+1, n):
            if a[j] > a[max_i]:
                max_i = j
        a[i], a[max_i] = a[max_i], a[i],


d = [2, 4, 5, 1, 3]
sel_sort(d)
print(d)
