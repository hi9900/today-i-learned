# 병합 정렬
# 입력: 리스트 a
# 출력: 없음(입력으로 주어진 a가 정렬됨)
def merge_sort(a):
    n = len(a)

    # 자료 개수가 한 개 이하면 반환
    if n <= 1:
        return a

    # 중간 지점을 기준으로 앞, 뒤 나눔
    mid = n // 2
    g1 = a[:mid]
    g2 = a[mid:]
    merge_sort(g1)
    merge_sort(g2)

    # 병합
    # g1과 g2의 정렬하지 않은 맨 앞 인덱스
    i1 = 0
    i2 = 0
    # 정렬 할 인덱스
    k = 0
    # 리스트가 남아있으면,
    while i1 < len(g1) and i2 < len(g2):
        # 작은 값을 k로
        if g1[i1] < g2[i2]:
            a[k] = g1[i1]
            i1 += 1
        else:
            a[k] = g2[i2]
            i2 += 1
        k += 1

    # 한 쪽에만 남아있으면, 모두 넣기
    while i1 < len(g1):
        a[k] = g1[i1]
        i1 += 1
        k += 1
    while i2 < len(g2):
        a[k] = g2[i2]
        i2 += 1
        k += 1


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
merge_sort(d)
print(d)
