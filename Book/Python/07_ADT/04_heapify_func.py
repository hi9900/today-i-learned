import heapq

list1 = [4, 6, 8, 1]

# 리스트를 힙으로 변환
heapq.heapify(list1)
print(list1)    # [1, 4, 8, 6]

# 항목을 힙에 삽입
h = []
heapq.heappush(h, (1, 'food'))
heapq.heappush(h, (2, 'have fun'))
heapq.heappush(h, (3, 'work'))
heapq.heappush(h, (4, 'study'))

print(h)    
# [(1, 'food'), (2, 'have fun'), (3, 'work'), (4, 'study')]

# 힙에서 가장 작은 항목을 제거하고 반환
print(heapq.heappop(list1))    # 1
print(list1)        # [4, 6, 8]

# 새 항목을 힙에 추가한 후,; push
# 가장 작은 항목을 제거하고 반환; pop
# heapq.heappushpop(heap, item)

# 힙의 가장 작은 항목을 제거하고 반환 후; pop
# 새 항목을 추가; push
# heapq.heapreplace(heap, item)

# 여러 개의 정렬된 반복 가능한 객체를 병합하여 
# 하나의 정렬된 결과의 이터레이터 반환
for x in heapq.merge([1, 3, 5], [2, 4, 6]):
    print(x, end=" ")
    # 1 2 3 4 5 6

# 데이터(반복 가능한 객체에 의해 정의된)에서
# n개의 가장 큰 요소와 
# heapq.nlargest(n, iterable[, key])
# 가장 작은 요소가 있는 리스트 반환
# heapq.nsmallest(n, iterable[, key])