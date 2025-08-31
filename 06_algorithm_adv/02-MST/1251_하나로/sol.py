import sys
sys.stdin = open('1251_inputs.txt')

from itertools import combinations
import heapq

def prim(start):
    global min_sum

    visited = set()
    visited.add(start) # 방문체크
    min_heap = [(w, start, e) for e, w in adj_list[start]]
    heapq.heapify(min_heap) # 최소힙 만들기

    while min_heap:
        weight, start, end = heapq.heappop(min_heap)
        if end in visited: continue # 이미 방문했으면 갈 필요 없음

        visited.add(end)
        min_sum += weight

        for next, weight in adj_list[end]:
            # 이미 방문한 곳이면 넣을 필요도 없음
            if next in visited: continue
            heapq.heappush(min_heap, (weight, end, next))


T = int(input())
for t in range(1, T+1):
    N = int(input())
    Xs = list(map(int, input().split()))
    Ys = list(map(int, input().split()))
    E = float(input())

    vers = [i for i in range(N)]
    adj_list = {v: [] for v in range(N)}

    min_sum = 0

    """
    프림으로 풀거다 -> 그럼 가중치 필요함
    모든 N에 대한 조합들을 만들어서 가중치 그래프를 만들어야 함
    adj_list = {v:[] for v in range(N)}
    """
    for comb in combinations(vers, 2): # 인덱스로 정점의 조합들을 만들어 냄
        v1, v2 = comb # ex. 0, 1
        dist = (Xs[v1] - Xs[v2])**2 + (Ys[v1] - Ys[v2])**2
        adj_list[v1].append((v2, dist))
        adj_list[v2].append((v1, dist))

    prim(0)
    print(f"#{t} {round(E * min_sum)}")

