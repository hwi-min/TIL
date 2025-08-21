import sys
sys.stdin = open('sample_input.txt')


def find_set(x):
    if x == students[x]: # 노드가 x 자기 자신을 부모로 가지면 그대로 반환
        return x
    return find_set(students[x]) # 아닌 경우 최상위 노드까지 탐색

def union(x, y):
    # 두 집합 합치기
    root_x = find_set(x)
    root_y = find_set(y)
    if root_x != root_y:
        students[root_y] = root_x

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    pairs = list(map(int, input().split())) # (1, 2) (3, 4)

    students = [i for i in range(N+1)] # parents 정보 저장

    for i in range(0, len(pairs), 2):
        x, y = pairs[i], pairs[i+1]
        union(x, y)






