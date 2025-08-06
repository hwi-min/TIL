# 정점 정보
#         0    1    2    3    4    5    6
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# 간선 정보
edges = [
    '0 1',
    '0 2',
    '1 3',
    '1 4',
    '2 4',
    '3 5',
    '4 5',
    '5 6'
]

adj_matrix = [[0] * len(nodes) for _ in range(len(nodes))]
print(adj_matrix)
for edge in edges:
    u, v = edge.split()
    u_idx, v_idx = int(u), int(v)
    print(u_idx, v_idx)
    adj_matrix[u_idx][v_idx] = 1
    adj_matrix[v_idx][u_idx] = 1
print(adj_matrix)


from collections import deque

## BFS
def BFS(start_vertex):
    # 해당 정점 방문 여부 표시할 배열이 하나 필요하다
    # visited = [0] * len(nodes)
    visited = set()
    # 후보군을 저장
    queue = deque([start_vertex]) # deque는 첫 인자로 iterable 객체를 받는다.
    visited.add(start_vertex)
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in adj_list.get(node, []):
            # 해당 정점 아직 방문한적 없다면
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor) # 다음 후보군에 추가
    return result