# 친구 리스트에서 자신의 모든 친구를 찾는 알고리즘
# 입력: 친구 관계 그래프 g, 모든 친구를 찾을 자신 start
# 출력: 모든 친구의 이름
def print_all_friends(g, start):
    # 앞으로 처리할 사람
    qu = [start]
    # 이미 큐에 추가한 사람
    done = set()
    done.add(start)

    # 큐에 사람이 남아있다면,
    while qu:
        friend = qu.pop(0)
        print(friend)
        for qu_friend in g[friend]:
            if qu_friend not in done:
                qu.append(qu_friend)
                done.add(qu_friend)


# 친구 관계 리스트
# A와 B가 친구이면
# A의 친구 리스트에도 B가 나오고, B의 친구 리스트에도 A가 나옴
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
