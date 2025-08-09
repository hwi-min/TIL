import sys
sys.stdin = open('./SWEA_data_inputs/input1.txt')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().strip().split())
    pic = [list(map(int, input().strip().split())) for _ in range(N)]

    for i in range(N): # N개의 행을 순회하며
        for j in range(M): # M개의 열을 순회하며
            if pic[i][j] == 1:
                while 
