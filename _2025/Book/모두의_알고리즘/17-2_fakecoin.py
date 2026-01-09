# 주어진 동전 n개 중에 가짜 동전(fake)을 찾아내는 알고리즘
# 입력: 전체 동전 위치의 시작과 끝(0, n - 1)
# 출력: 가짜 동전의 위치 번호

# 무게 재기 함수
# a에서 b까지에 놓인 동전과
# c에서 d까지에 놓인 동전의 무게를 비교
# a에서 b까지에 가짜 동전이 있으면(가벼우면): -1
# c에서 d까지에 가짜 동전이 있으면(가벼우면): 1
# 가짜 동전이 없으면(양쪽 무게가 같으면): 0
def weigh(a, b, c, d):
    fake = 29  # 가짜 동전의 위치(알고리즘은 weigh() 함수를 이용하여 이 값을 맞혀야 함)
    if a <= fake and fake <= b:
        return -1
    if c <= fake and fake <= d:
        return 1
    return 0


# weigh() 함수(저울질)를 이용하여
# left와 right까지에 놓인 가짜 동전의 위치를 찾아냄
def find_fakecoin(left, right):
    # 가짜동전 범위에 동전이 하나면, 그 동전이 가짜
    if left == right:
        return left

    # 두 그룹으로 나누기
    # 홀수면 하나가 남음 (right)
    half = (right - left + 1) // 2
    g1_l, g1_r = left, left + half - 1
    g2_l = left + half
    g2_r = g2_l + half - 1

    result = weigh(g1_l, g1_r, g2_l, g2_r)
    if result == -1:
        return find_fakecoin(g1_l, g1_r)
    elif result == 1:
        return find_fakecoin(g2_l, g2_r)
    else:
        return right


n = 100    # 전체 동전 개수
print(find_fakecoin(0, n - 1))
