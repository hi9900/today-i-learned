# n명에서 두 명을 뽑아 짝을 만드는 모든 경우를 찾는 알고리즘
# 입력: n명의 이름이 들어 있는 리스트
# 출력: 두 명을 뽑아 만들 수 있는 모든 짝
def print_pairs(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n):
            print(f"{lst[i]} - {lst[j]}")


name = ["Tom", "Jerry", "Mike"]
print_pairs(name)
print()
name2 = ["Tom", "Jerry", "Mike", "John"]
print_pairs(name2)
