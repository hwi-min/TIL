import sys
sys.stdin = open('./SWEA_input_datas/input_1248.txt')

def bfs()

T = int(input())
for t in range(1, T+1):
    # 정점개수, 간선개수, 타겟정점1, 타겟정점2
    V, E, n1, n2 = map(int, input().strip().split())
    infos = list(map(int, input().strip().split()))
    parents = [0] * (V+1)
    children = [[] for _ in range(V+1)] # 1-based이므로 V+1개 생성

    for i in range(0, len(infos), 2):
        parents[infos[i]] = infos[i+1]
        children[]

    print(tree)


