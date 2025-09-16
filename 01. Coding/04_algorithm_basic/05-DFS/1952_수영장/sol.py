import sys
sys.stdin = open('sample_input.txt')

def dfs(month_idx, current_sum):
    global min_price_sum

    # 마지막 idx까지 돌면 마무리
    if month_idx > 11:
        # min_price_sum보다 current_sum이 작으면 최소값 업데이트
        if min_price_sum > current_sum: min_price_sum = current_sum
        return

    # 가지치기: 현재까지의 합이 이미 최소 값보다 크면 그만 탐색
    if current_sum > min_price_sum: return


    # 1일권을 선택하는 경우
    dfs(month_idx+1, current_sum+months[month_idx]*one_day)

    # 1달권을 선택하는 경우
    dfs(month_idx+1, current_sum+month)

    # 3달권을 선택하는 경우
    dfs(month_idx+3, current_sum+month_3)


T = int(input())
for t in range(1, T+1):
    one_day, month, month_3, one_year = map(int, input().split())
    months = list(map(int, input().split()))
    min_price_sum = 3000 * 31 * 12 # 최악의 경우 하루권이 3000원이고 매달 매일가는 경우

    dfs(0, 0)

    if min_price_sum < one_year:
        print(f"#{t} {min_price_sum}")
    else: print(f"#{t} {one_year}")




