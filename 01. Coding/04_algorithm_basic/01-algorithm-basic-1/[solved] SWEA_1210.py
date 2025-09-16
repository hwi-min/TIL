import sys
sys.stdin = open('./SWEA_input_datas/input_1210.txt')

direction = [(-1, 0), (0, -1), (0, 1)] # 상, 좌, 우

T = 10
for t in range(1, T+1):
    _ = int(input())
    ladder = [list(map(int, input().strip().split())) for _ in range(100)]
    visited = [[False] * 100 for _ in range(100)]

    # 도착지점 찾기
    end_x = 99
    end_y = ladder[end_x].index(2)

    while end_x > 0:
        if end_y -1 >= 0 and not visited[end_x][end_y-1] and ladder[end_x][end_y-1] == 1:
            end_y -= 1

        elif end_y + 1 < 100 and not visited[end_x][end_y+1] and ladder[end_x][end_y+1] == 1:
            end_y = end_y + 1
        elif end_x -1 >= 0 and not visited[end_x-1][end_y] and ladder[end_x-1][end_y] == 1:
            end_x = end_x -1


