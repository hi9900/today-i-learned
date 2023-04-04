# 친구 리스트에서 자신의 모든 친구를 찾고 친구들의 친밀도를 계산하는 알고리즘
# 입력: 친구 관계 그래프 g, 모든 친구를 찾을 자신 start
# 출력: 모든 친구의 이름과 자신과의 친밀도
def print_all_friends(g, start):
    # 앞으로 처리할 사람과 그사람과의 친밀도
    qu = [(start, 0)]
    # 이미 큐에 추가한 사람
    done = set()
    done.add(start)

    while qu:
        friend, w = qu.pop(0)
        print(friend, w)
        for qu_friend in g[friend]:
            if qu_friend not in done:
                qu.append((qu_friend, w+1))
                done.add(qu_friend)


fr_info = {
    'Summer': ['John', 'Justin', 'Mike'],
    'John': ['Summer', 'Justin'],
    'Justin': ['John', 'Summer', 'Mike', 'May'],
    'Mike': ['Summer', 'Justin'],
    'May': ['Justin', 'Kim'],
    'Kim': ['May'],
    'Tom': ['Jerry'],
    'Jerry': ['Tom']
}

print_all_friends(fr_info, 'Summer')
print()
print_all_friends(fr_info, 'Jerry')
