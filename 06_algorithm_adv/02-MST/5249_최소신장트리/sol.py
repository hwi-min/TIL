import sys
sys.stdin = open('5249_inputs.txt')
#
# # kruskal
#
# def find_set(x):
#     if x != parents[x]:
#         parents[x] = find_set(parents[x])
#
#     return parents[x]
#
# def union(x, y):
#     rep_x, rep_y = find_set(x), find_set(y)
#     if rep_x != rep_y:
#         if rank[rep_x] > rank[rep_y]:
#             parents[rep_y] = rep_x
#         elif rank[rep_x] < rank[rep_y]:
#             parents[rep_x] = rep_y
#         else:
#             parents[rep_y] = rep_x
#             rank[rep_x] += 1
#         return True
#     return False
#
# T = int(input())
# for t in range(1, T+1):
#     V, E = map(int, input().split())
#     edges = []
#     parents = [i for i in range(V+1)]
#     rank = [0 for _ in range(V+1)]
#     min_sum = 0
#
#     for _ in range(E):
#         n1, n2, w = map(int, input().split())
#         edges.append((n1, n2, w))
#
#     edges.sort(key=lambda x: x[2])
#
#     for n1, n2, w in edges:
#         if union(n1, n2):
#             min_sum += w
#
#     print(f"#{t} {min_sum}")
#

# prim
"""
임의의 정점에서 시작하면 됨
- heap을 만들어서 최소힙을 구성
- [시작점, weight(가중치)]
- visited = set()
"""
import heapq

def prim(start):
    global min_sum
    visited = set()

    min_heap = [(w, start, e) for e, w in adj_list[start]]
    heapq.heapify(min_heap) # 가중치 기준 최소힙
    visited.add(start)

    while min_heap:
        weight, start, end = heapq.heappop(min_heap)
        if end in visited: continue
        visited.add(end)
        min_sum += weight

        for next, weight in adj_list[end]:
            if next in visited: continue
            heapq.heappush(min_heap, (weight, end, next))



T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    # 각 정점에 대한 인접 리스트 생성
    adj_list = {v: [] for v in range(V+1)}
    min_sum = 0

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj_list[n1].append((n2, w))
        adj_list[n2].append((n1, w))

    prim(0)
    print(f"#{t} {min_sum}")