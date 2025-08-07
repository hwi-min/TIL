import sys
sys.stdin = open('./SWEA_input_datas/sample_input_5215.txt')

def dfs(idx, score_sum, cal_sum):
    global max_sum

    if cal_sum > L: # 제한 칼로리보다 현재까지의 칼로리 합이 크면 안됨
        return

    if idx == N: # 전체 재료를 다 돌았으면 탈출
        max_sum = max(max_sum, score_sum)
        return

    dfs(idx+1, score_sum+score[idx], cal_sum+calorie[idx]) # 이번 재료를 선택한 경우
    dfs(idx+1, score_sum, cal_sum) # 이번 재료를 선택하지 않은 경우


T = int(input())
for t in range(1, T+1):
    N, L = map(int, input().strip().split()) # 재료의 수, 제한 칼로리
    score, calorie = [], [] # 맛에 대한 점수, 칼로리 리스트 초기화

    # 맛, 칼로리를 받아서 리스트에 저장
    for _ in range(N):
        s, c = map(int, input().strip().split())
        score.append(s)
        calorie.append(c)

    max_sum = 0 # 최대
    dfs(0, 0, 0)

    print(f"#{t} {max_sum}")