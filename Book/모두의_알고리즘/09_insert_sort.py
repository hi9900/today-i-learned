# 삽입 정렬
# 입력: 리스트 a
# 출력: 없음(입력으로 주어진 a가 정렬됨)

def ins_sort(a):
    n = len(a)
    for i in range(1, n):
        # i번 값을 저장
        tmp = a[i]
        # j는 i바로 왼쪽부터
        j = i-1
        # j번 값이 i번째 값보다 크다면, i값이 j보다 왼쪽에 가야함
        while j >= 0 and a[j] > tmp:
            # i번째 값은 저장해놨으니, j값을 한 칸 오른쪽으로 밀기
            a[j+1] = a[j]
            # 다음 조사 대상은 왼쪽
            j -= 1
        # while 에서 벗어난 j+1은 i값이 들어갈 위치
        a[j+1] = tmp


d = [2, 4, 5, 1, 3]
ins_sort(d)
print(d)
