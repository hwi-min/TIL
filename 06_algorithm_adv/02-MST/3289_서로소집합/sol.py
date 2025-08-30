import sys
sys.stdin = open('3289_inputs.txt')

"""
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫째 줄에 n(1≤n≤1,000,000), m(1≤m≤100,000)이 주어진다.

m은 입력으로 주어지는 연산의 개수이다.

다음 m개의 줄에는 각각의 연산이 주어진다.

합집합은 0 a b의 형태로 입력이 주어진다.

이는 a가 포함되어 있는 집합과, b가 포함되어 있는 집합을 합친다는 의미이다.

두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 1 a b의 형태로 입력이 주어진다.

이는 a와 b가 같은 집합에 포함되어 있는지를 확인하는 연산이다.

a와 b는 n 이하의 자연수이며 같을 수도 있다.

1
7 8

0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

각 테스트 케이스마다 1로 시작하는 입력에 대해서 같은 집합에 속해있다면 1을, 아니면 0을 순서대로 한줄에 연속하여 출력한다.

"""

# 0 -> 합치겠다 / 1 -> 같은 집합에 포함되어있는지 확인
def find_set(x):
    # 내가 그룹의 대표자가 아니면
    if x != rep[x]:
        rep[x] = find_set(rep[x])
    return rep[x]

def union(x, y):
    rep_x, rep_y = find_set(x), find_set(y)
    if rep_x != rep_y:
        if rank[rep_x] > rank[rep_y]:
            rep[rep_y] = rep_x
        elif rank[rep_x] < rank[rep_y]:
            rep[rep_x] = rep_y
        else:
            rep[rep_y] = rep_x
            rank[rep_x] += 1

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    rep = [i for i in range(n+1)]
    rank = [0 for _ in range(n+1)]

    result = ""
    for _ in range(m):
        command, g1, g2 = map(int, input().split())
        if command == 0:
            union(g1, g2)
        else: # 같은 집합인지 확인
            if find_set(g1) != find_set(g2):
                result += '0'
            else: result += '1'

    print(f"#{t} {result}")
