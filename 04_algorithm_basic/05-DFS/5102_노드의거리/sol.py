import sys
sys.stdin = open('5102_inputs.txt')

from collections import deque

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    graph = {v:[] for v in range(1, V+1)}
    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    S, G = map(int, input().split())
    visited = [False] * (V+1)


    queue = deque([(S, 0)])
    visited[S] = True
    answer = 0

    while queue:
        current, dist = queue.popleft()

        if current == G:
            answer = dist
            break

        for neighbor in graph[current]:
            # 방문하지 않은 노드라면
            if not visited[neighbor]:
                queue.append((neighbor, dist+1))
                visited[neighbor] = True

    print(f"#{t} {answer}")


