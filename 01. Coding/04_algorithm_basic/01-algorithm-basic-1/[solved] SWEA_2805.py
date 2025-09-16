import sys
sys.stdin = open('./SWEA_input_datas/input_2805.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input().strip())) for _ in range(N)]
    mid = N // 2 # 중간 지점
    crop_sum = 0 # 농작물의 합 초기화

    # 0번 행 ~ mid 행까지 값 더하기
    for i in range(0, mid+1): # mid 행까지
        for x in range(mid-i, mid+i+1):
            crop_sum += int(farm[i][x])

    # mid+1 행부터 마지막 행까지
    for i in range(mid+1, N):
        for x in range(mid - (N - i - 1), mid + (N - i - 1) + 1):
            crop_sum += int(farm[i][x])

    print(f"#{t} {crop_sum}")

