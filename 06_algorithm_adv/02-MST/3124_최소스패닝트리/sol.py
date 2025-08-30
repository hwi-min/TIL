import sys
sys.stdin = open('3124_inputs.txt')


def find_set(x):
    if x != parents[x]:
        parents[x] = find_set(parents[x])

    return parents[x]

def union(x, y):
    rep_x, rep_y = map

T = int(input())
for _ in range(1, T+1):
    V, E = map(int, input().split())
    parents = [i for i in range(V+1)]
    ranks = [0 for _ in range(V+1)]
    visited = set()
    edges = []
    min_sum = 1000000 * E # 최악의 경우

    for _ in range(E):
        n1, n2, w = map(int, input().split()) # w: 음수일수도 있다 !
        edges.append((n1, n2, w))

    # 가중치가 낮은 것부터 높은 것으로 오름차순 정렬
    edges.sort(key=lambda x: x[2])

    for n1, n2, w in edges:
        union(n1, n2)




