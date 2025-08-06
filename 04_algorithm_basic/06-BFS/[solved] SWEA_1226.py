import sys
sys.stdin = open('./SWEA_input_datas/input_1226.txt')

from collections import deque

# 방향 정의
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(grid, start_x, start_y):
    global end_x, end_y

    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True # 방문처리

    while queue:
        current_x, current_y = queue.popleft()

        # 도착점에 도달하면 1 반환
        if current_x == end_x and current_y == end_y:
            return 1

        for (dx, dy) in direction: # 4방향으로 이동
            nx, ny = current_x + dx, current_y + dy

            if 0 <= nx < 16 and 0 <= ny < 16 and not visited[nx][ny]:
                if grid[nx][ny] != 1: # == 0으로 설정하면 3을 도달하지 못함 !!!
                    visited[nx][ny] = True # 방문처리
                    queue.append((nx, ny))

    return 0

T = 10
for t in range(1, T+1):
    _ = int(input())
    grid = [list(map(int, input().strip())) for _ in range(16)]
    visited = [[False] * 16 for _ in range(16)]
    start_x, start_y, end_x, end_y = -1, -1, -1, -1

    # 시작점, 도착점 찾기
    for x in range(16):
        for y in range(16):
            if grid[x][y] == 2: start_x, start_y = x, y
            elif grid[x][y] == 3: end_x, end_y = x, y
            if start_x != -1 and start_y != -1 and end_x != -1 and end_y != -1:
                break

    result = bfs(grid, start_x, start_y)
    print(f"#{t} {result}")