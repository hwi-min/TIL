import sys
sys.stdin = open('./SWEA_data_inputs/input1.txt')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().strip().split())
    pic = [list(map(int, input().strip().split())) for _ in range(N)]
    max_ruins = 0

    # 가로 방향 탐색
    for i in range(N): # N개의 행을 순회하며
        sub_ruins = 0
        for j in range(M): # M개의 열을 순회하며
            if pic[i][j] == 1: sub_ruins += 1 # 해당 위치에 유적이 존재하면(1) ruins 1 증가
            else:
                if sub_ruins > max_ruins: max_ruins = sub_ruins # sub_ruins가 max_ruins보다 크면 업데이트
                sub_ruins = 0 # 그렇지 않으면, 더이상 유적이 없다는 의미이므로 sub_ruins를 0으로 다시 초기화
        if sub_ruins > max_ruins:

