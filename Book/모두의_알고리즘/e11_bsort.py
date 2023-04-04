# 거품 정렬
# 입력: 리스트 a
# 출력: 없음(입력으로 주어진 a가 정렬됨)
def bubble_sort(a):
    n = len(a)
    changed = True
    while changed:
        changed = False
        for i in range(n-1):
            if a[i] > a[i+1]:
                print(a)
                a[i], a[i+1], = a[i+1], a[i]
                changed = True


d = [2, 4, 5, 1, 3]
bubble_sort(d)
print(d)
