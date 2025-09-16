import sys
sys.stdin = open('./SWEA_input_datas/input_1220.txt')

## flag로 풀이
T = 10
for t in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for j in range(N):  # column 기준으로 순회
        flag = False # 교착상태 가능성을 나타내는 flag

        for i in range(N):  # row 순차적으로 순회
            if grid[i][j] == 1: # 1이 등장하는 순간 교착 가능 상태가 됨
                flag = True # 교착상태 가능성 True
            elif grid[i][j] == 2: # 2가 등장하면
                if flag: # 교착 가능한 상태일때 2를 만나면
                    cnt += 1 # 교착상태 +1
                    flag = False # 교착 가능성을 다시 False

    print(f"#{t} {cnt}")

## stack으로 풀이
T = 10
for t in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for j in range(N):  # column 기준으로 순회
        stacked = []
        for i in range(N):  # row 순차적으로 순회
            if grid[i][j] == 1 and not stacked: # 1이 등장 & 스택이 비어있으면
                stacked.append(grid[i][j]) # 요소를 추가
            elif grid[i][j] == 2: # 2가 등장하고
                if stacked: # stack에 요소 (1)가 존재할때
                    cnt += 1 # 교착상태 +1
                    stacked.pop() # 요소(1)를 pop

    print(f"#{t} {cnt}")