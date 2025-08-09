import sys
sys.stdin = open('./SWEA_input_datas/sample_input_5178.txt')

T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().strip().split())
    tree = [0] * (N+1)

    # input받아온 리프번호와 숫자 tree에 삽입
    for _ in range(M):
        leaf, num = map(int, input().split())
        tree[leaf] = num

    for i in range(N, 0, -1):
        if i*2 <= N and i*2+1 <=N: tree[i] = tree[i*2] + tree[i*2+1]
        if i*2 <= N and i*2+1 > N: tree[i] = tree[i*2]

    print(f"#{t} {tree[L]}")