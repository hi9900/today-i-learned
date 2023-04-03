# 쉽게 설명한 병합 정렬
# 입력: 리스트 a
# 출력: 정렬된 새 리스트
def merge_sort(a):
    n = len(a)

    # 자료 개수가 한 개 이하면 반환
    if n <= 1:
        return a

    # 중간 지점을 기준으로 앞, 뒤 나눔
    mid = n // 2
    g1 = merge_sort(a[:mid])
    g2 = merge_sort(a[mid:])

    result = []
    # 두 그룹에 자료가 남아 있으면,
    while g1 and g2:
        # 작은 값을 먼저 저장
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))

    # 하나라도 비어있으면, 남은 값들을 모두 저장
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(merge_sort(d))
