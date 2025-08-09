import sys
sys.stdin = open('./SWEA_input_datas/sample_input_4836.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    grid = [[0] * 10 for _ in range(10)] # 빈 10*10 grid 초기화
    result = 0

    # N개의 영역을 모두 받아오며
    for _ in range(N):
        # 왼쪽 위 서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2, color
        r1, c1, r2, c2, color = map(int, input().strip().split())

        for i in range(c1, c2+1):
            for j in range(r1, r2+1):
                grid[i][j] += color

    for i in range(10):
        for j in range(10):
            if grid[i][j] == 3:
                result += 1

    print(f"#{t} {result}")

