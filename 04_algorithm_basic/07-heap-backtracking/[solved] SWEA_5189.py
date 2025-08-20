import sys
sys.stdin = open('./SWEA_input_datas/sample_input_5189.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    track = [list(map(int, input().strip().split())) for _ in range(N)]
    visited = [False] * N

    dfs(idx, )