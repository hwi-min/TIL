def fibonacci_memoization(n):
    # n이 2 이상이고, memo[n]번째가 아직 계산되지 않았으면
        # 계산을 할 것이다.
    if n >= 2 and memo[n] == 0:
        memo[n] = fibonacci_memoization(n-1) + fibonacci_memoization(n-2)
    # 만약 예전에 계산한 적이 있다면, 그걸 그냥 그대로 가져다 쓴다
    return memo[n]

# 피보나치 수 10개를 기록하고 싶다.
n = 10
# 10개의 값을 기록? lsit
memo = [0] * (n+1) # 0부터 10까지 11개
# 피보나치의 기본룰
memo[0], memo[1] = 0, 1 # 기본 룰 초기화

# 사용 예시
print(fibonacci_memoization(10)) # 55를

