import sys
sys.stdin = open('3124_inputs.txt')


def find_set(x):
    if x != parents[x]:
        parents[x] = find_set(parents[x])

    return parents[x]

def union(x, y):
    rep_x, rep_y = find_set(x), find_set(y)
    if rep_x != rep_y:
        if ranks[rep_x] > ranks[rep_y]:
            parents[rep_y] = rep_x
        elif ranks[rep_x] < ranks[rep_y]:
            parents[rep_x] = rep_y
        else:
            parents[rep_y] = rep_x
            ranks[rep_x] += 1
        return True
    return False

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    parents = [i for i in range(V+1)]
    ranks = [0 for _ in range(V+1)]
    visited = set()
    edges = []
    min_sum = 0

    for _ in range(E):
        n1, n2, w = map(int, input().split()) # w: 음수일수도 있다 !
        edges.append((n1, n2, w))

    # 가중치가 낮은 것부터 높은 것으로 오름차순 정렬
    edges.sort(key=lambda x: x[2])

    for n1, n2, w in edges:
        if union(n1, n2):
            min_sum += w
    print(f"#{t} {min_sum}")




