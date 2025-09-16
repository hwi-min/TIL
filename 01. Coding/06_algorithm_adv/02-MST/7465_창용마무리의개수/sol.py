import sys
sys.stdin = open('7465_inputs.txt')

def find_set(x):
    # 두 사람의 대표자가 다르다면
    if x != rep[x]:
        rep[x] = find_set(rep[x]) # x사람의 대표자를 대표자로 세우고 반
    return rep[x]

def union(x, y):
    rep_x, rep_y = find_set(x), find_set(y)

    # 두 대표가 다르면 union 가능!
    if  rep_x != rep_y:
        if rank[rep_x] > rank[rep_y]: # rep_x의 높이가 더 높으면
            rep[rep_y] = rep_x
        elif rank[rep_x] < rank[rep_y]:
            rep[rep_x] = rep_y
        else: # rank가 동일한 경우에는 앞에 있는 애를 대표로 세우자
            rep[rep_y] = rep_x
            rank[rep_x] += 1

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    rep = [i for i in range(N+1)]
    rank = [0 for _ in range(N+1)]

    for _ in range(M):
        p1, p2 = map(int, input().split())
        union(p1, p2)

    groups = set()
    for p in range(1, N+1):
        groups.add(find_set(p))

    print(f"#{t} {len(groups)}")

