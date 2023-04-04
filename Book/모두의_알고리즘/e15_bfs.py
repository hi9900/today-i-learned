# 그래프 탐색: 너비 우선 탐색
# 입력: 그래프 g, 탐색 시작점 start
# 출력: start에서 출발해 연결된 꼭짓점들을 출력
def bfs(g, start):
    q = []
    done = set()

    q.append(start)
    done.add(start)

    while q:
        x = q.pop(0)
        print(x)
        for i in g[x]:
            if i not in done:
                q.append(i)
                done.add(i)


# 그래프 정보
g = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

bfs(g, 1)
