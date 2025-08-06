import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(row, col, acc):
    global min_count

    if row == N-1 and col == M-1: # 도착지다
        min_count = min(min_count, acc) # 여기까지 도달하는데 돈 비용과 최소값을 비교
        return

    for k in range(4):
        nx, ny = row + dx[k], col + dy[k]

        # 범위를 벗어나거나, 방문한적 있거나, 아니면 패스~
        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if visited[nx][ny]: continue
        if not road[nx][ny]: continue

        # 갈 수 있으면 방문 표시하고 이동
        visited[nx][ny] = 1
        dfs(nx, ny, acc+1)

# 입력 처리
N, M = map(int, input().split())
road = [list(map(int, input())) for _ in range(N)]

# 방문 배열 및 최소 이동 횟수 초기화
visited = [[False] * M for _ in range(N)]
min_count = float('inf')

# 시작점 방문처리 후 탐색 시작
visited[0][0] = True
dfs(0, 0, 0)

print(min_count)  # 결과 출력
