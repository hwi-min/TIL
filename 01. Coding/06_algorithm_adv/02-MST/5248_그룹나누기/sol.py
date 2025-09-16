import sys
sys.stdin = open('5248_inputs.txt')

# def find_set(x):
#     # 자신이 속한 그룹의 대표가 자신이면
#     if x == representatives[x]:
#         return x
#     # 아니면, 대표자를 찾아서 반
#     return find_set(representatives[x])

# 경로 압축 버전 find_set(x)
def find_set(x):
    # 자신이 그룹의 대표자가 아니라면
    if x != representatives[x]:
        representatives[x] = find_set(representatives[x])
    return representatives[x]

def union(x, y):
    x_rep, y_rep = find_set(x), find_set(y)

    # 두 대표자가 같으면 -> 이미 같은 그룹이므로 union 불가
    # 두 대표자가 다르면 -> 같은 그룹으로 union 가
    if x_rep != y_rep:
        # x_rep의 랭크가 더 높다면 ... x_rep에 union해줌
        if ranks[x_rep] > ranks[y_rep]:
            representatives[y_rep] = x_rep
        # x_rep의 랭크가 더 높다면 ... x_rep에 union해줌
        elif ranks[x_rep] < ranks[y_rep]:
            representatives[x_rep] = y_rep
        else: # 두 랭크가 비슷하다면 -> 그냥 앞에 애를 대표로 만들겠음
            representatives[y_rep] = x_rep
            ranks[x_rep] += 1

        # if else를 최적화해서 코드 줄일 수 있을듯??

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    edges = list(map(int, input().split()))
    representatives = [i for i in range(N+1)]
    ranks = [0 for _ in range(N+1)] # ranks가 반드시 필요한가???

    # 간격 2씩 증가하면서 ...
    for i in range(0, len(edges), 2):
        union(edges[i], edges[i+1])

    # 몇개의 그룹이 만들어 졌는지 확인 -> representatives의 unique한 값이 몇개인지 찾으면 됨
    groups = set()
    for j in range(1, N+1):
        groups.add(find_set(j))

    print(f"#{t} {len(groups)}")