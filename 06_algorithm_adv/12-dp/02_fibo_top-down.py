def fibo(N):
    global cnt
    cnt += 1
    if N >= 2 and memo[N] == 0:
        # memo[N] = memo[N-1] + memo[N-2]
        memo[N] = fibo(N-1) + fibo(N-2)
    # N이 0이거나 1인 경우
    return memo[N]


memo = [0] * (101) # 기록을 할 리스트
# f(100)을 얻기 위해서는 f(99), f(98)을 얻을 수 있어야 하듯
memo[0] = 0
memo[1] = 1
cnt = 0
result = fibo(100)
print(result)
print(cnt)